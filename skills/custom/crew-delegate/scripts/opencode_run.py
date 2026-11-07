#!/usr/bin/env python3
"""Run a task through the OpenCode CLI on its free models, with fallback and an optional QA pass.

Usage:
  opencode_run.py --task "..." [--model opencode/deepseek-v4.1-flash-free] [--cwd DIR] [--verify]
                  [--session ID] [--timeout 1800] [--no-auto] [--chain m1,m2,...] [--text]
                  [--vision]

The task text may be "@path/to/file.md". Same exit codes as agy_run.py:
0 success, 2 task failed on every model, 3 verify FAIL, 4 timeout (partial output).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

OPENCODE = os.path.expanduser("~/.opencode/bin/opencode")

# Free OpenCode Zen models, strongest coder first (measured 2026-11-01).
DEFAULT_CHAIN = [
    "opencode/deepseek-v4.1-flash-free",
    "opencode/glm-5.3-flash-free",
    "opencode/mimo-v2.6-flash-free",
    "opencode/big-pickle",
    "opencode/flint-40b-free",
    "opencode/nemotron-3.5-lightning-free",
    "opencode/beam-free",
    "opencode/crouton-alpha-free",
    "opencode/pulse-alpha-free",
    # Google free tier allows 16k input tokens per minute: one agent step, so last resort.
    "google/gemma-4-31b-it",
    "google/gemma-4-26b-a4b-it",
]
# Only free model that reads images; put first for screenshot/vision tasks.
VISION_MODEL = "opencode/nemotron-3.5-super-vl-free"

LIMIT_RE = re.compile(
    r"usage limit|quota|rate.?limit|too many requests|\b429\b|resource.?exhausted|exhausted|"
    r"limit (reached|exceeded)|capacity|overloaded|\b503\b|\b502\b|\b529\b|unavailable|"
    r"try again later|subscribe to opencode go|switch models|insufficient|credits",
    re.I,
)

VERIFY_SCHEMA_TEXT = (
    'Return ONLY a JSON object, no prose, no code fence: {"verdict": "PASS" or "FAIL", '
    '"evidence": [strings], "missing": [strings], "notes": string}.'
)


def log(msg):
    print(f"[opencode_run] {msg}", file=sys.stderr, flush=True)


def run_opencode(prompt, model, args, auto, session=None, agent=None, timeout=None):
    cmd = [OPENCODE, "run", "--format", "json", "-m", model]
    if auto:
        cmd.append("--auto")
    if session:
        cmd += ["-s", session]
    if agent:
        cmd += ["--agent", agent]
    cmd.append(prompt)
    t0 = time.time()
    tmo = timeout if timeout is not None else args.timeout
    try:
        # stdin closed: opencode must never wait on a terminal in headless runs.
        proc = subprocess.run(cmd, cwd=args.cwd, capture_output=True, text=True,
                              stdin=subprocess.DEVNULL,
                              timeout=tmo if tmo and tmo > 0 else None)
        out, err, rc, timed_out = proc.stdout, proc.stderr, proc.returncode, False
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        err = (e.stderr or b"").decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
        rc, timed_out = -1, True
    texts, errors, session_id, tokens, reason = [], [], "", {"input": 0, "output": 0, "reasoning": 0}, ""
    for line in out.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        session_id = ev.get("sessionID") or session_id
        part = ev.get("part") or {}
        t = ev.get("type")
        if t == "text":
            texts.append(part.get("text", ""))
        elif t == "error":
            e = ev.get("error") or {}
            errors.append(f"{e.get('type','')}: {e.get('message','')}".strip(": "))
        elif t == "step_finish":
            reason = part.get("reason", reason)
            for k in tokens:
                tokens[k] += (part.get("tokens") or {}).get(k, 0)
    response = texts[-1].strip() if texts else ""
    blob = " ".join(errors) + " " + err.strip()
    data = {
        "model": model,
        "session_id": session_id,
        "response": response,
        "all_text": "\n\n".join(texts),
        "error": " | ".join(errors) if errors else "",
        "stderr": err.strip()[-1500:],
        "finish_reason": reason,
        "exit_code": rc,
        "usage": tokens,
        "wall_seconds": round(time.time() - t0, 1),
    }
    if timed_out:
        data["status"], data["finished_reason"] = "SUCCESS", "print_timeout"
    elif errors or (not response and not texts):
        data["status"] = "ERROR"
        if not data["error"]:
            data["error"] = err.strip()[-500:] or "empty response"
    elif LIMIT_RE.search(response) and len(response) < 300:
        # The free tier reports limits as a plain text part, not an error event.
        data["status"], data["error"] = "ERROR", response
    else:
        data["status"], data["finished_reason"] = "SUCCESS", ""
    return data


def with_fallback(prompt, chain, args, auto, session=None, agent=None, timeout=None):
    attempts = []
    for model in chain:
        log(f"model {model}")
        data = run_opencode(prompt, model, args, auto, session, agent, timeout)
        attempts.append({"model": model, "status": data["status"],
                         "finished_reason": data.get("finished_reason", ""),
                         "error": (data.get("error") or "")[:300],
                         "wall_seconds": data["wall_seconds"]})
        if data["status"] == "SUCCESS" and data.get("finished_reason") != "print_timeout":
            data["attempts"] = attempts
            return data
        if data.get("finished_reason") == "print_timeout":
            log(f"timeout on {model}; no fallback (session {data['session_id']} may still be running)")
            data["attempts"] = attempts
            return data
        blob = f"{data.get('error','')} {data.get('stderr','')}"
        if LIMIT_RE.search(blob):
            log(f"limit/capacity on {model}: {blob.strip()[:160]!r}; falling back")
            session = None  # a new model starts a new session
            continue
        log(f"hard error on {model}: {blob.strip()[:300]!r}")
        data["attempts"] = attempts
        return data
    return {"status": "ERROR", "error": "all models in chain failed on limits",
            "response": "", "session_id": "", "model": chain[-1], "attempts": attempts}


def build_chain(model, chain_arg, vision=False):
    chain = [m.strip() for m in chain_arg.split(",") if m.strip()] if chain_arg else list(DEFAULT_CHAIN)
    if vision:
        chain = [VISION_MODEL] + [m for m in chain if m != VISION_MODEL]
    if model:
        if "/" not in model:
            model = "opencode/" + model
        chain = [model] + [m for m in chain if m != model]
    return chain


def parse_verdict(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                return None
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True, help="prompt text, or @file")
    ap.add_argument("--model", default=None, help="first model (default opencode/deepseek-v4.1-flash-free)")
    ap.add_argument("--chain", default=None, help="comma list overriding the fallback chain")
    ap.add_argument("--vision", action="store_true", help="put the vision-capable free model first")
    ap.add_argument("--cwd", default=os.getcwd())
    ap.add_argument("--session", default=None, help="resume (or create) this opencode session id")
    ap.add_argument("--timeout", type=int, default=1800, help="seconds; 0 = wait")
    ap.add_argument("--no-auto", action="store_true",
                    help="do not pass --auto (headless opencode then cannot use tools that need approval)")
    ap.add_argument("--verify", action="store_true",
                    help="second pass with the read-only plan agent that checks the work")
    ap.add_argument("--verify-model", default=None)
    ap.add_argument("--text", action="store_true")
    args = ap.parse_args()

    task = args.task
    if task.startswith("@"):
        with open(task[1:], encoding="utf-8") as fh:
            task = fh.read()

    chain = build_chain(args.model, args.chain, args.vision)
    result = with_fallback(task, chain, args, auto=not args.no_auto, session=args.session)
    summary = {
        "status": result["status"],
        "worker": "opencode",
        "model_used": result.get("model"),
        "session_id": result.get("session_id", ""),
        "finished_reason": result.get("finished_reason", ""),
        "response": result.get("response", ""),
        "error": result.get("error", ""),
        "usage": result.get("usage"),
        "attempts": result.get("attempts", []),
    }
    code = 0
    if result["status"] != "SUCCESS":
        code = 2
    elif result.get("finished_reason") == "print_timeout":
        code = 4

    if args.verify and code == 0:
        verify_prompt = (
            "You are a QA worker. Another worker claims it finished a task in this workspace "
            f"(cwd: {args.cwd}). Check the claim with read-only tools: read files, run git diff/status, "
            "run tests or builds that do not modify tracked files. Do not fix anything.\n\n"
            f"TASK GIVEN TO THE WORKER:\n{task}\n\nWORKER REPORT:\n{summary['response']}\n\n"
            "Verdict PASS only if every requirement in the task is visibly done; list concrete "
            f"evidence (file:line, command output) and anything missing. {VERIFY_SCHEMA_TEXT}"
        )
        vchain = build_chain(args.verify_model, args.chain)
        # The built-in "plan" agent is read-only; --auto lets its read/shell tools run.
        vres = with_fallback(verify_prompt, vchain, args, auto=True, agent="plan")
        verdict = parse_verdict(vres.get("response", "") or "")
        summary["verify"] = {
            "status": vres["status"],
            "model_used": vres.get("model"),
            "session_id": vres.get("session_id", ""),
            "verdict": verdict,
            "raw": None if verdict else (vres.get("response", "") or vres.get("error", ""))[:2000],
            "attempts": vres.get("attempts", []),
        }
        if not verdict or verdict.get("verdict") != "PASS":
            code = 3

    if args.text:
        print(summary["response"])
        if "verify" in summary:
            print("\n--- verify ---")
            print(json.dumps(summary["verify"].get("verdict") or summary["verify"], indent=2))
    else:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    sys.exit(code)


if __name__ == "__main__":
    main()

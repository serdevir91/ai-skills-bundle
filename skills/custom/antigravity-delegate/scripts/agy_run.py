#!/usr/bin/env python3
"""Run a task through the Antigravity CLI (agy) with model fallback and an optional QA pass.

Usage:
  agy_run.py --task "..." [--model gemini-4-argon-high] [--cwd DIR] [--verify]
             [--conversation ID] [--effort low|medium|high|xhigh|max]
             [--timeout 1800] [--no-yolo] [--add-dir DIR ...] [--json-schema FILE|JSON]
             [--chain m1,m2,...] [--text]

The task text may be "@path/to/file.md" to read the prompt from a file.

Exit codes: 0 success (and verify PASS when --verify), 2 task failed on every model,
3 verify FAIL, 4 print timeout (partial output).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

DEFAULT_CHAIN = [
    "gemini-4-argon-high",
    "gemini-4-argon-medium",
    "gemini-4-argon-low",
    "claude-opus-5-5-high",
    "claude-sonnet-5-5-high",
    "gemini-3.8-flash-high",
    "gpt-oss-120b-medium",
]

# Errors that mean "this model is out of budget / busy": move to the next model.
LIMIT_RE = re.compile(
    r"quota|rate.?limit|too many requests|\b429\b|resource.?exhausted|exhausted|"
    r"usage limit|limit (reached|exceeded)|capacity|overloaded|\b503\b|unavailable|"
    r"try again later|deadline exceeded|\b502\b|\b529\b",
    re.I,
)

VERIFY_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
        "evidence": {"type": "array", "items": {"type": "string"}},
        "missing": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "string"},
    },
    "required": ["verdict", "evidence", "missing"],
}


def log(msg):
    print(f"[agy_run] {msg}", file=sys.stderr, flush=True)


def run_agy(prompt, model, args, yolo, conversation=None, json_schema=None, timeout=None,
            sandbox=False):
    cmd = ["agy", "-p", prompt, "--model", model, "--output-format", "json",
           "--print-timeout", f"{timeout or args.timeout}s"]
    if yolo:
        cmd.append("--dangerously-skip-permissions")
    if sandbox:
        cmd.append("--sandbox")
    if conversation:
        cmd += ["--conversation", conversation]
    if args.effort:
        cmd += ["--effort", args.effort]
    for d in args.add_dir:
        cmd += ["--add-dir", d]
    if args.project:
        cmd += ["--project", args.project]
    if json_schema:
        cmd += ["--json-schema", json_schema]
    t0 = time.time()
    proc = subprocess.run(cmd, cwd=args.cwd, capture_output=True, text=True,
                          stdin=subprocess.DEVNULL)
    out = proc.stdout.strip()
    # agy prints diagnostics before the JSON on some paths; take the last JSON object.
    data = None
    for line in reversed(out.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                data = json.loads(line)
                break
            except json.JSONDecodeError:
                continue
    if data is None:
        data = {"status": "ERROR", "error": (proc.stderr or out or "no output").strip()[-2000:],
                "response": "", "conversation_id": ""}
    data.setdefault("error", "")
    # A denied tool call ends the turn with an empty response; surface it as an error.
    if data.get("status") == "SUCCESS" and not (data.get("response") or "").strip() \
            and not data.get("structured_output") and data.get("finished_reason") != "print_timeout":
        denied = [d.get("display_name", d.get("action", "?")) for d in data.get("denied_actions", [])]
        data["status"] = "ERROR"
        data["error"] = ("empty response; denied tool calls: " + ", ".join(denied)) if denied \
            else "empty response"
    data["model"] = model
    data["exit_code"] = proc.returncode
    data["wall_seconds"] = round(time.time() - t0, 1)
    if proc.stderr.strip() and data["status"] != "SUCCESS":
        data["stderr"] = proc.stderr.strip()[-2000:]
    return data


def with_fallback(prompt, chain, args, yolo, conversation=None, json_schema=None, timeout=None,
                  sandbox=False):
    attempts = []
    for model in chain:
        log(f"model {model}")
        data = run_agy(prompt, model, args, yolo, conversation, json_schema, timeout, sandbox)
        attempts.append({"model": model, "status": data["status"],
                         "finished_reason": data.get("finished_reason", ""),
                         "error": (data.get("error") or "")[:300],
                         "wall_seconds": data["wall_seconds"]})
        if data["status"] == "SUCCESS" and data.get("finished_reason") != "print_timeout":
            data["attempts"] = attempts
            return data
        if data.get("finished_reason") == "print_timeout":
            log(f"print timeout on {model}; no fallback (task may still be running)")
            data["attempts"] = attempts
            return data
        blob = f"{data.get('error','')} {data.get('stderr','')} {data.get('response','')}"
        if LIMIT_RE.search(blob):
            log(f"limit/capacity error on {model}: {blob.strip()[:160]!r}; falling back")
            continue
        log(f"hard error on {model}: {blob.strip()[:300]!r}")
        data["attempts"] = attempts
        return data
    return {"status": "ERROR", "error": "all models in chain failed on limits",
            "response": "", "conversation_id": "", "model": chain[-1], "attempts": attempts}


def build_chain(model, chain_arg):
    chain = [m.strip() for m in chain_arg.split(",") if m.strip()] if chain_arg else list(DEFAULT_CHAIN)
    if model:
        chain = [model] + [m for m in chain if m != model]
    return chain


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True, help="prompt text, or @file")
    ap.add_argument("--model", default=None, help="first model to try (default gemini-4-argon-high)")
    ap.add_argument("--chain", default=None, help="comma list overriding the fallback chain")
    ap.add_argument("--cwd", default=os.getcwd())
    ap.add_argument("--conversation", default=None, help="resume this agy conversation id")
    ap.add_argument("--effort", default=None)
    ap.add_argument("--timeout", type=int, default=1800, help="print timeout seconds (0 = wait)")
    ap.add_argument("--no-yolo", action="store_true",
                    help="do not pass --dangerously-skip-permissions (headless agy then denies tool calls)")
    ap.add_argument("--add-dir", action="append", default=[])
    ap.add_argument("--project", default=None)
    ap.add_argument("--json-schema", default=None)
    ap.add_argument("--verify", action="store_true",
                    help="run a second, read-only agy pass that checks the work like an Antigravity QA worker")
    ap.add_argument("--verify-model", default=None, help="first model for the verify pass")
    ap.add_argument("--text", action="store_true", help="print only the response text")
    args = ap.parse_args()

    task = args.task
    if task.startswith("@"):
        with open(task[1:], encoding="utf-8") as fh:
            task = fh.read()

    chain = build_chain(args.model, args.chain)
    result = with_fallback(task, chain, args, yolo=not args.no_yolo,
                           conversation=args.conversation, json_schema=args.json_schema)
    summary = {
        "status": result["status"],
        "model_used": result.get("model"),
        "conversation_id": result.get("conversation_id", ""),
        "finished_reason": result.get("finished_reason", ""),
        "response": result.get("response", ""),
        "structured_output": result.get("structured_output"),
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
            "You are an Antigravity QA worker. Another worker claims it finished a task in this "
            f"workspace (cwd: {args.cwd}). Check the claim with read-only tools only: read files, run "
            "git diff/status, run tests or builds that do not modify tracked files. Do not fix anything.\n\n"
            f"TASK GIVEN TO THE WORKER:\n{task}\n\nWORKER REPORT:\n{summary['response']}\n\n"
            "Return JSON: verdict PASS only if every requirement in the task is visibly done; list "
            "concrete evidence (file:line, command output) and anything missing."
        )
        vchain = build_chain(args.verify_model, args.chain)
        # Sandbox: commands run with terminal restrictions, so the checker can read and
        # run tests but is kept from editing the tree. Without yolo every command is denied.
        vres = with_fallback(verify_prompt, vchain, args, yolo=True, sandbox=True,
                             json_schema=json.dumps(VERIFY_SCHEMA))
        verdict = vres.get("structured_output")
        try:
            if not verdict:
                verdict = json.loads(vres.get("response", "") or "null")
        except json.JSONDecodeError:
            m = re.search(r"\{.*\}", vres.get("response", ""), re.S)
            if m:
                try:
                    verdict = json.loads(m.group(0))
                except json.JSONDecodeError:
                    verdict = None
        summary["verify"] = {
            "status": vres["status"],
            "model_used": vres.get("model"),
            "conversation_id": vres.get("conversation_id", ""),
            "verdict": verdict,
            "raw": None if verdict else vres.get("response", "")[:2000],
            "error": vres.get("error", ""),
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

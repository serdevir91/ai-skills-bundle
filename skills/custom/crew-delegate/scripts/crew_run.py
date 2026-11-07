#!/usr/bin/env python3
"""Boss router: send a task to Antigravity (agy) or OpenCode, with cross-worker fallback.

Usage:
  crew_run.py --task "...|@file" --cwd DIR [--worker auto|agy|opencode] [--kind heavy|light|vision]
              [--model ID] [--verify] [--timeout S] [--resume ID] [--text]

Routing with --worker auto:
  heavy  -> agy (Argon chain), falls back to opencode when every agy model is out of quota
  light  -> opencode free chain, falls back to agy when every free model is out of quota
  vision -> opencode nemotron-3.5-super-vl-free first
Exit codes follow the worker wrappers: 0 ok, 2 failed, 3 verify FAIL, 4 timeout.
"""
import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AGY = os.path.expanduser("~/.claude/skills/antigravity-delegate/scripts/agy_run.py")
OPENCODE = os.path.join(HERE, "opencode_run.py")


def log(msg):
    print(f"[crew] {msg}", file=sys.stderr, flush=True)


def run_worker(worker, args, resume=None):
    script = AGY if worker == "agy" else OPENCODE
    cmd = [sys.executable, script, "--task", args.task, "--cwd", args.cwd, "--timeout", str(args.timeout)]
    if args.model:
        cmd += ["--model", args.model]
    if args.verify:
        cmd.append("--verify")
    if resume:
        cmd += ["--conversation" if worker == "agy" else "--session", resume]
    if worker == "opencode" and args.kind == "vision":
        cmd.append("--vision")
    if worker == "agy" and args.effort:
        cmd += ["--effort", args.effort]
    log(f"worker {worker}")
    proc = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    sys.stderr.write(proc.stderr)
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        data = {"status": "ERROR", "error": (proc.stdout or proc.stderr)[-1500:], "attempts": []}
    data["worker"] = worker
    data["exit_code"] = proc.returncode
    return data


def all_limits(data):
    """True when the worker gave up because every model in its chain hit a limit."""
    return data.get("status") != "SUCCESS" and "all models in chain failed on limits" in (data.get("error") or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--cwd", default=os.getcwd())
    ap.add_argument("--worker", choices=["auto", "agy", "opencode"], default="auto")
    ap.add_argument("--kind", choices=["heavy", "light", "vision"], default="heavy")
    ap.add_argument("--model", default=None, help="first model for the chosen worker")
    ap.add_argument("--effort", default=None, help="agy only")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--resume", default=None, help="agy conversation id or opencode session id")
    ap.add_argument("--text", action="store_true")
    args = ap.parse_args()

    if args.worker != "auto":
        order = [args.worker]
    elif args.kind == "heavy":
        order = ["agy", "opencode"]
    else:
        order = ["opencode", "agy"]
    if args.resume:
        order = order[:1]

    results = []
    data = None
    for i, worker in enumerate(order):
        data = run_worker(worker, args, args.resume)
        results.append({"worker": worker, "status": data.get("status"), "model_used": data.get("model_used"),
                        "error": (data.get("error") or "")[:200]})
        if data.get("status") == "SUCCESS":
            break
        if i + 1 < len(order) and all_limits(data):
            log(f"{worker} chain exhausted; handing the task to {order[i + 1]}")
            args.model = None  # the other worker has its own model ids
            continue
        break

    data["routing"] = results
    if args.text:
        print(f"[{data.get('worker')} / {data.get('model_used')}]")
        print(data.get("response", "") or data.get("error", ""))
        if data.get("verify"):
            print("\n--- verify ---")
            print(json.dumps(data["verify"].get("verdict") or data["verify"], indent=2))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    sys.exit(data.get("exit_code", 2))


if __name__ == "__main__":
    main()

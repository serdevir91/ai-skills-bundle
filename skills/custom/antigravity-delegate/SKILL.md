---
name: antigravity-delegate
description: >-
  Delegate a coding or ops task to the Antigravity CLI (agy) running a chosen
  model, with automatic fallback when the model's usage limit or capacity is hit,
  then check the result like an Antigravity QA worker. Use when the user says
  "antigravity'ye yaptır", "agy ile yap", "use antigravity", "delegate to argon",
  "run this with Argon/Opus/Flash in Antigravity", or wants work offloaded to
  another agent while keeping control of the verification.
---

# Antigravity delegate

Run tasks through `agy` (Antigravity CLI, `~/.local/bin/agy`) on a model the
user picks, fall back to other models when the first one is out of quota, and
verify the outcome as an independent Antigravity worker before reporting.

## See also

`crew-delegate` (`~/.claude/skills/crew-delegate/`) is the boss-level
skill: it routes heavy work here and light work to the OpenCode free models,
with cross-worker fallback. Use `crew_run.py` unless a task must go to agy.

## Auto-delegation policy (standing instruction, 2026-11-01)

The user does not want to ask for delegation each time. On every task, split the
work yourself and hand the Antigravity-sized parts to `agy` without asking:

Purpose: Claude's throughput. Workers take grunt work only; Claude keeps the
heavy, judgment-bound work (architecture, core logic, tricky features,
debugging, tests).

Delegate by default (grunt work):
- Boilerplate screens and files written from a spec Claude already wrote,
  baseline features copied from a reference app (update check, review prompt,
  paywall), mechanical refactors with a clear rule.
- Scaffolding a new project from a template and the rename pass.
- Builds, `xcodebuild` archives, `flutter build`, lint fixes.
- Generating store copy, listing JSON, release notes, privacy/support HTML.
- Long mechanical sweeps (localization files, asset renames, bulk edits).
- Independent parts of one task run as parallel `agy_run.py` processes, each in
  its own folder, never two writers on the same files.

Keep here (never delegate):
- Architecture, data model, core game/app logic, algorithms, tricky UI,
  performance work, anything that needs the conversation's context.
- Anything touching credentials, API keys, keychains, signing, uploads to
  Play/ASC/TestFlight/MS Store, `git push`, deletes outside the project.
- Browser work in Chrome (ASC web UI, Unity dashboard, GitHub Pages settings).
- Decisions, planning, splitting the work, and the final verification.
- Testing (unit tests, UI tests, simulator/emulator runs, screenshots) and
  every bug fix, including bugs in Antigravity's own output: Antigravity writes
  features, Claude tests them and fixes what breaks. Do not resume an agy
  conversation to fix a bug; fix it here.

Verification is always yours: `--verify` plus your own `git status`, build or
test run, and a read of the files the report cites, before reporting done.
Report which parts Antigravity did and on which model.

## Default model and fallback order

1. `gemini-4-argon-high` (default; "Argon")
2. `gemini-4-argon-medium`
3. `gemini-4-argon-low`
4. `claude-opus-5-5-high`
5. `claude-sonnet-5-5-high`
6. `gemini-3.8-flash-high`
7. `gpt-oss-120b-medium`

Fallback happens only on limit/capacity errors (quota, rate limit, 429, 503,
RESOURCE_EXHAUSTED, overloaded, unavailable). A hard error (bad prompt, tool
failure, invalid model) stops the chain and is reported as-is. The user may
name a model ("Opus ile yap") → that model goes first, the rest of the chain
stays as fallback. `agy models` lists the live ids.

## Commands

Wrapper (preferred; handles fallback, JSON parsing, verify pass):

```bash
python3 ~/.claude/skills/antigravity-delegate/scripts/agy_run.py --task "<task>" --cwd <project> --verify
```

Options:
- `--model <id>` first model; `--chain a,b,c` custom order.
- `--task @file.md` reads a long prompt from a file (write briefs to the scratchpad first).
- `--conversation <id>` resumes an earlier agy conversation (id is in every result).
- `--effort low|medium|high|xhigh|max`.
- `--timeout <s>` print timeout (default 1800; 0 = wait forever). On timeout the
  result has `finished_reason: print_timeout` and exit code 4; resume with
  `--conversation` and ask for the status.
- `--no-yolo` drops `--dangerously-skip-permissions`. Headless `agy` auto-denies
  every tool call without it, so keep yolo for any task that edits files or
  runs commands; use `--no-yolo` only for pure Q&A.
- `--add-dir <dir>` extra workspace folders; `--project <name>`.
- `--json-schema <file|json>` for structured output.
- `--text` prints only the response (plus the verify verdict).

Raw CLI, when the wrapper does not fit:

```bash
agy -p "<prompt>" --model gemini-4-argon-high --output-format json --dangerously-skip-permissions --print-timeout 1800s
```

Result JSON fields: `conversation_id`, `status` (SUCCESS | ERROR), `response`,
`error`, `finished_reason` (`error` | `print_timeout` | absent), `usage`.

## Workflow

1. **Brief.** Write the task as a self-contained brief: goal, files/dirs, the
   exact "done" condition, constraints from the workspace rules (English UI,
   baseline update/review/IAP features, no physical-device claims). Save long
   briefs to a file and pass `--task @file`.
2. **Run.** Call `agy_run.py` with `--cwd` set to the project folder. Run it in
   the background when it may exceed two minutes. Read `model_used` and
   `attempts` to know which model did the work and whether fallback happened.
3. **Verify as an Antigravity worker.** `--verify` runs a second `agy` pass in
   `--sandbox` (terminal restrictions, yolo on so reads and test commands run)
   with a QA prompt and a JSON schema: `{verdict: PASS|FAIL, evidence[],
   missing[]}`; the verdict comes from `structured_output`. Exit code 3 means
   FAIL. A pass whose tool call was denied ends with an empty response; the
   wrapper reports that as `empty response; denied tool calls: RunCommand`.
   Independently of that pass, check the decisive artifacts yourself: `git -C
   <cwd> status --short`, `git diff --stat`, run the build or tests the task
   named, open the files the report cites. Never report "done" from the
   worker's text alone.
4. **Fix.** On FAIL, a missing feature (work never done) may go back to the
   same conversation once: `--conversation <id> --task "Finish: ..."`. Bugs
   and failing tests are fixed here, never sent back.
5. **Report.** Model used, fallbacks taken, conversation id, what was verified
   and how, what is still open.

## Guardrails

- `--dangerously-skip-permissions` lets agy run any command. Only delegate
  tasks whose blast radius is the project folder: no credentials, no store
  uploads, no git push, no deletes outside the project. Do those steps yourself.
- Headless agy has no interactive login: if `status` is ERROR with
  "not logged in" / auth text, tell the user to run `agy` once in a terminal.
- `--mode auto` is not available on this account; `--mode plan` and
  `accept-edits` work.
- Keep each delegated task to one project and one outcome; chain several runs
  rather than one giant brief.
- Workspace skills for agy live in `.agents/skills/<name>/SKILL.md`; global ones
  in `~/.claude/skills/`. Antigravity also reads `AGENTS.md`, so the
  workspace rules already apply inside the delegated run.

---
name: crew-delegate
description: >-
  Boss/worker setup: Claude plans, splits and verifies; Antigravity CLI (agy,
  Argon first) and OpenCode CLI (free Zen models) do the delegated coding work.
  Use on every non-trivial task without being asked ("sen patronsun"): decide
  the split, route heavy code to Antigravity and light/mechanical work to
  OpenCode, fall back across workers on quota limits, then test and fix here.
  Triggers: any feature, scaffold, build, store-copy or bulk-edit task; "agy",
  "opencode", "antigravity", "görev paylaşımı", "çalışanlara ver".
---

# Crew delegate

Standing instruction (2026-11-01): the user does not want to ask. Claude is the
boss; Antigravity and OpenCode are the workers. The purpose is Claude's
throughput: workers take the grunt work ("amelelik") so Claude's context and
time go to the hard parts. Claude keeps the heavy, judgment-bound work itself:
architecture, core game/app logic, tricky features, anything that needs the
conversation's context, all testing, all bug fixing. On every task Claude
decides the split, starts the workers in the background, does the hard part
meanwhile, and verifies everything before reporting.

## Workers

| Worker | CLI | Models | Best for |
|---|---|---|---|
| Antigravity | `agy` | `gemini-4-argon-high` → argon-medium → argon-low → `claude-opus-5-5-high` → `claude-sonnet-5-5-high` → `gemini-3.8-flash-high` → `gpt-oss-120b-medium` | large grunt work: scaffold + rename passes, boilerplate screens from a spec Claude wrote, baseline features copied from a reference app, mechanical multi-file edits, builds and archives |
| OpenCode | `~/.opencode/bin/opencode` | free Zen: `opencode/deepseek-v4.1-flash-free` (free here, unlike OpenRouter) → `glm-5.3-flash-free` → `mimo-v2.6-flash-free` → `big-pickle` → `flint-40b-free` → `nemotron-3.5-lightning-free` → `beam-free` → `crouton-alpha-free` → `pulse-alpha-free` → `google/gemma-4-31b-it` → `google/gemma-4-26b-a4b-it` (16k tokens/min, last resort, needs Google key in OpenCode); vision: `nemotron-3.5-super-vl-free` | small grunt work: store copy, listing JSON, HTML pages, localization sweeps, one-file scripts, renames, docs, screenshot reading |

Not delegated at all: architecture and data model, core game/app logic,
algorithms, tricky UI, performance work, anything that needs the context of
this conversation, debugging, tests. Those are Claude's own work.

Both wrappers return the same JSON summary (`status`, `model_used`,
`response`, `attempts`, optional `verify`) and the same exit codes:
0 ok, 2 failed on every model, 3 verify FAIL, 4 timeout.

## Commands

Router (preferred):

```bash
python3 ~/.claude/skills/crew-delegate/scripts/crew_run.py --task @brief.md --cwd ~/Code/<app> --kind heavy --verify --text
```

- `--kind heavy` → large grunt job: agy first, OpenCode when every agy model is out of quota.
- `--kind light` → small grunt job: OpenCode free chain first, agy when the free tier is exhausted.
- `--kind vision` → OpenCode `nemotron-3.5-super-vl-free` first (image input).
- `--worker agy|opencode` pins a worker; `--model <id>` pins its first model.
- `--resume <id>` continues an agy conversation id or an opencode session id.
- `--verify` adds the QA pass (agy: `--sandbox` run; opencode: `--agent plan`).

Direct wrappers:

```bash
python3 ~/.claude/skills/antigravity-delegate/scripts/agy_run.py --task @brief.md --cwd DIR --verify
```

```bash
python3 ~/.claude/skills/crew-delegate/scripts/opencode_run.py --task @brief.md --cwd DIR --verify
```

Raw OpenCode: `opencode run --auto --format json -m opencode/<model> "<prompt>"`
(`-s <id>` resumes; `--agent plan` is read-only). Without `--auto` headless
runs cannot use tools. The free tier reports limits as a plain text reply
("usage limit reached … switch models"); the wrapper treats that as a limit
and moves to the next model. `opencode models` lists the live ids.

## Boss workflow

1. **Split in one line.** Claude takes the hard core; workers get the grunt
   parts that need no judgment. Name which part goes where before any
   delegated call; the user should not have to ask. If a task has no grunt
   part, no worker is started.
2. **Brief per worker task.** Self-contained: goal, folder, files, "done"
   condition, workspace rules that matter (English UI, baseline update/review/
   IAP, no physical-device claims). Save to the scratchpad and pass `@file`.
3. **Run in the background.** One worker process per independent part, each in
   its own folder. Two workers never write the same files. Both workers at once
   when the parts are independent.
4. **Keep here, never delegate:** credentials, signing, keychains, store uploads
   (Play/ASC/TestFlight/MS Store), `git push`, deletes outside the project,
   Chrome work (ASC web, Unity dashboard, GitHub Pages), planning, the split,
   and all testing and bug fixing. Workers write features and build; Claude
   runs unit/UI tests, simulators, screenshots, and fixes every bug, including
   bugs in a worker's output. Do not send bugs back to a worker.
5. **Verify yourself.** `--verify` is a hint, not proof. Check `git status`,
   `git diff --stat`, run the build or tests the task named, read the files the
   report cites. Report which worker and model did each part.
6. **Fallback order on limits:** Argon → other agy models → OpenCode free →
   stop and tell the user. A missing feature (never done) may go back once with
   `--resume`; a bug is fixed here.

## Routing rules of thumb

- Grunt test: could a careful junior do it from the brief alone, with no
  design decision? Yes → delegate. No → Claude does it.
- Scaffold/rename passes, boilerplate screens from Claude's spec, baseline
  features copied from a reference app, bulk multi-file mechanical edits,
  builds/archives: heavy grunt → Antigravity.
- Text, JSON, HTML, Python one-file scripts, bulk mechanical edits, lint
  cleanups, first drafts of docs: light grunt → OpenCode (free; keep Argon's budget).
- Core logic, architecture, tricky features, debugging, tests: Claude, always.
- Reading screenshots or images: vision → OpenCode `nemotron-3.5-super-vl-free`.
- Argon busy or over quota and the task is urgent: light the task down and send
  it to OpenCode, or run the remaining part here.
- Free models are weaker: give them small, exact briefs with the target file
  path and an example of the expected output; review their diff line by line.

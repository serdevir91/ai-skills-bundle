---
name: hermes-delegate
description: >-
  Offload work to a remote server with the SSH alias `hermes`: Hermes Agent on OpenRouter free models, web scraping with Scrapling, long ffmpeg or batch jobs, anything that must survive the Mac sleeping. Use without being asked when a job is long, heavy or public-data research. Triggers: "hermes", "sunucu", "sunucuda yap", "hermes'e yaptır", "uzak sunucu".
---

# Hermes delegate

Claude stays lead: plan here, hand off, then verify the result here before reporting it.

## Run

One-shot agent job, free models with automatic fallback:

```bash
ssh hermes '~/.local/bin/hermes-free "prompt"'
```

Output starts with `[model: <id>]`. Set `HERMES_FREE_TIMEOUT` (seconds, default 600) for longer jobs. Set `HERMES_MODEL=<id>` to use only that model. `deepseek/deepseek-v4.1-flash` is the last fallback and is billed, not free.

Long job, survives disconnects:

```bash
ssh hermes 'tmux new -d -s job1 "~/.local/bin/hermes-free \"prompt\" > ~/job1.log 2>&1"'
```

Direct commands on the server, no model involved:

```bash
ssh hermes 'scrapling extract get https://example.com /tmp/a.md'
```

Move files with `rsync -a <src> hermes:<dst>`.

## Fit

- Good: scraping public pages, research, bulk text, ffmpeg, batch jobs, always-on tasks, Ollama.
- Keep on the Mac: iOS builds, store uploads, credentials, browser sign-ins, core logic, bug fixes.
- Adjust to your own server: watch memory on big jobs. Set up the `hermes` SSH alias and a `hermes-free` wrapper first.

## Rules

- Send no secrets, keys or private data in prompts: free models may log them.
- Leave live services on the server alone.
- Scraping: a 403, 429, challenge or CAPTCHA means stop and report.

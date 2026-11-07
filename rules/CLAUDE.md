# CLAUDE.md / Agent Guidelines

## Mandatory App Baseline (All Apps & Frameworks: Flutter, Godot, React, Native, etc.)

For EVERY application, game, or project developed or updated:
- **New Projects**: Must implement In-App Update, In-App Review, and In-App Purchase (IAP/Paywall) by default from day 1.
- **Existing Projects**: Whenever any existing project is updated, refactored, or given a new feature/version, if any of these three features are missing, they MUST be implemented during that update.

### Core Baseline Requirements:
1. **In-App Update**: Automatic silent startup check + manual "Check for Updates" action in settings/menu.
2. **In-App Review & Rating**: Dynamic rating prompt upon milestone events + manual "Rate App" / "Write Review" button in settings/menu.
3. **In-App Purchase (IAP) & Paywall**: Dedicated Pro/Premium Paywall screen, product purchase flow, mandatory "Restore Purchases" button, secure offline entitlement persistence, and transparent error handling.
4. **Theme Support**: Light, dark, and pure-black (AMOLED) modes with persistent state across restarts.

## Context Rules (Token Saving)
- Never read whole files; grep first, then read only the relevant lines (offset/limit).
- Delegate broad codebase research to a subagent; return only the conclusion.
- Build/test output: show only error lines (pipe through filters, e.g. `| grep -iE error`).
- Keep summaries of changes short.
- Keep tool-call descriptions, status lines, and messages as short as possible.
- MCP tools and skills: load only when needed. Load deferred tools via ToolSearch on demand; never preload unused ones.

## Compact Instructions
When summarizing: keep code changes made, open errors, and decisions; drop file contents and tool outputs.


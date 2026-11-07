# Install guide for AI agents

Kullanım: Bu dosyanın linkini kendi yapay zekana ver ve "Buradaki talimatlarla skilleri kur" de.

You are an AI agent. The user wants the skills in this repository installed. Follow these steps.

## Steps

1. Clone the repository to a temporary folder:

   ```bash
   git clone --depth 1 https://github.com/serdevir91/ai-skills-bundle.git /tmp/ai-skills-bundle
   ```

2. Find the skills folder for the agent you are running in:

   | Agent | Target |
   |---|---|
   | Claude Code | `~/.claude/skills` |
   | Codex | `~/.codex/skills` |
   | Other agent with a skills folder | That agent's documented folder |
   | Agent with no skills support | Skip the install. Load the relevant `SKILL.md` files as instructions or knowledge files |

3. List what is available:

   ```bash
   /tmp/ai-skills-bundle/install.sh --list
   ```

4. Ask the user which groups or skills they want, unless they already said. Recommend only what they need. A large install crowds the agent's context.

   | Group | Contents |
   |---|---|
   | `custom` | Store publishing, Flutter baseline and audit, agent delegation, scraping, reverse engineering |
   | `workflow` | Short answers, careful coding, review and verification workflows |
   | `firebase` | Firebase, Firestore and Xcode setup |
   | `anthropic` | Design, documents, MCP building, testing |
   | `community` | About 190 role skills: engineering, product, marketing, compliance |

5. Install. Use your target from step 2:

   ```bash
   /tmp/ai-skills-bundle/install.sh --target ~/.claude/skills custom workflow
   ```

   Existing skills are skipped. Add `--force` only if the user agrees to replace them.

6. Optional: offer the rules in `rules/`. Do not overwrite the user's own `AGENTS.md` or `CLAUDE.md`. Show the differences and merge only what the user accepts.

7. Delete `/tmp/ai-skills-bundle`. Tell the user what was installed and that the agent may need a restart.

## Rules

- This repository holds no API keys. Values such as `<ISSUER_ID>`, `<KEY_ID>`, `<WORKSPACE>` and `com.example.myapp` are placeholders. Ask the user for their own values when a skill needs them, and keep those values out of the skill files.
- Read a skill's scripts before you run them.
- Publish skills expect the user's own `upload_to_*.py` scripts, which are not included.
- Delegation skills need their own tools: `agy`, `opencode`, or an SSH host named `hermes`. Their paths assume `~/.claude/skills`. Update the paths if you install elsewhere.

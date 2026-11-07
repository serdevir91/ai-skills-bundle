# Agent Context Handoff (agent.md)

## Context
When starting a new software project, creating a centralized knowledge file is crucial for passing context between different AI sessions or different agentic models over time.

## Instructions
1. For ANY newly created project or repository, immediately create an `agent.md` file in the root directory.
2. The `agent.md` file MUST contain:
   - **Project Goal**: A high-level summary of what the project does.
   - **Tech Stack**: The frontend, backend, database, and key libraries used.
   - **Architecture**: A brief outline of the folder structure (e.g., Clean Architecture, MVC).
   - **Key Workflows**: How the main features operate.
   - **Next Agent Instructions**: Any specific gotchas or rules the next agent needs to know.
3. Update this file whenever a major architectural change occurs.

---
name: reverse-engineer-anything
description: Deeply inspect, reverse engineer, and report on any repository, codebase, or application (native binaries, Android APKs, Electron/ASAR, .NET assemblies, web runtimes, and source code). Use whenever asked to inspect, analyze, or report on another GitHub repository, local project codebase, or compiled application.
metadata:
  version: "35"
  framework: "REA (Reverse Engineer Anything) + Repo Inspector"
---

# REA & Repository / Application Inspector

Use this skill whenever asked to inspect, analyze, reverse engineer, or report on:
1. **Source Code Repositories & Projects**: GitHub/GitLab repositories, local source folders, or multi-module application projects.
2. **Compiled Applications & Shipped Artifacts**: Native binaries (PE/ELF/Mach-O), Electron apps/ASAR packages, Android APKs, .NET assemblies, browser/web runtimes, and firmware images using REA (Reverse Engineer Anything).

---

## 1. Investigation Routing

Determine the target type:

| Target Category | Examples | Inspection Approach | Primary Tools |
|-----------------|----------|---------------------|---------------|
| **Source Repository / Codebase** | GitHub repo URL, local project folder | Static source exploration, AST, architecture mapping | Git / GitHub API, file viewing, code search, AST analysis |
| **Electron / JavaScript Package** | `.asar`, extracted JS bundle, web app | REA JavaScript static analysis & module graph | `analyze_javascript_application`, `inspect_analysis_view`, `trace_application_feature` |
| **Android Application** | `.apk` package | REA Android manifest & JADX decompilation | `inspect_android_package`, `search_android_classes`, `inspect_android_method` |
| **Native Executable / Library** | `.exe`, `.dll`, `.so`, `.dylib` | REA binary disassembler & decompilation | `open_binary`, `binary_overview`, `decompile_function`, `xrefs`, `search_strings` |
| **Managed .NET Assembly** | C# / .NET DLL or EXE | REA managed artifact inspection | `inspect_managed_artifact`, `verify_managed_native_boundaries` |
| **Package / Archive Inventory** | ZIP, MSIX, APPX, DMG | REA archive member analysis | `open_binary`, `inspect_artifact`, `compare_artifacts` |
| **Live Browser / Electron Web** | Open CDP port, web app | REA passive CDP observation | `list_browser_targets`, `capture_browser_page`, `capture_web_screenshot` |

---

## 2. Mode A: Source Repository & Codebase Analysis

When asked to inspect a GitHub repository or local codebase:

### Workflow
1. **Manifest & Stack Discovery**:
   - Locate and parse package managers / manifests (`package.json`, `pubspec.yaml`, `Cargo.toml`, `go.mod`, `pom.xml`, `requirements.txt`, `CMakeLists.txt`, etc.).
   - Identify language versions, core frameworks, build systems, and external dependencies.
2. **Entry Points & Bootstrapping**:
   - Find application entry points (`main.dart`, `index.ts`, `main.rs`, `Program.cs`, `app.py`, etc.).
   - Trace startup lifecycle: config loading, dependency injection, routing, middleware registration.
3. **Architectural Pattern & Directory Hierarchy**:
   - Map directory layout and determine architectural style (Clean Architecture, MVVM, Feature-first, Monorepo, Hexagonal, etc.).
   - Diagram module interactions and boundaries using Mermaid.
4. **Core Business Logic & Algorithms**:
   - Identify critical algorithms, math, data processing pipelines, or core features.
   - Trace control flow from trigger/UI down to database/network calls.
5. **Data Layer & State Management**:
   - Database schemas, ORMs, state stores (Riverpod, Redux, Zustand, Pinia, etc.), caching, serialization.
6. **APIs, IPC & External Boundaries**:
   - REST/GraphQL endpoints, gRPC protos, IPC channels, WebSocket events, CLI commands.
7. **Security, Reliability & Edge Cases**:
   - Authentication/authorization mechanisms, input validation, encryption, secret handling, error boundaries.

---

## 3. Mode B: Shipped Application & Artifact Analysis (REA Core)

When analyzing compiled binaries or shipped packages, apply REA's evidence-based reverse-engineering methodology.

### REA Connection & Diagnostics
REA runs locally via MCP or CLI fallback:
- **MCP Server**: registered as `rea` in client configuration (`mcp_config.json`).
- **CLI Commands**:
  ```bash
  # Check status & tools
  npx -y rea-agents@latest doctor --client antigravity --json
  # Inspect JavaScript / Electron ASAR
  npx -y rea-agents@latest analyze-javascript-application /path/to/app --json
  # Trace features
  npx -y rea-agents@latest trace-application-feature /path/to/app --feature <name>
  ```
- **Prerequisites Note**: REA connects to Hopper, Ghidra (12.1.x), or IDA if native decompilation is required. Static JS/Electron analysis requires no disassembler engine.

### Core REA Rules
1. **Work Summary-First**: Start with broad summary views, then narrow down using `inspect_analysis_view` or focused queries.
2. **Distinguish Observations vs. Inferences vs. Unknowns**:
   - *Observation*: Direct facts extracted from code, metadata, or decompilation with Evidence IDs.
   - *Inference*: Logical deductions supported by evidence.
   - *Unknown*: Areas requiring dynamic execution, unavailable debug symbols, or missing external servers.
3. **Clean Up**: Always call `close_binary` when finishing native disassembler sessions.

### On-Demand References
- Native binaries & assemblies: `references/native-and-artifacts.md`
- Electron & JavaScript packages: `references/javascript-applications.md`
- Android APKs & JADX: `references/android-applications.md`
- Passive browser observation: `references/runtime-observation.md`
- Evidence ledger & comparison: `references/evidence-workflows.md`

---

## 4. Standardized Deep Inspection Report Template

Always structure repository and application inspection reports following this template:

```markdown
# 🔍 [Repository / Application Name] - Technical Analysis & Inspection Report

## 1. Executive Summary
- **Overview**: 2-3 sentence high-level summary of the target's purpose, design, and domain.
- **Technology Stack**: Core languages, runtime, frameworks, key libraries, and build tools.
- **Architecture Highlights**: Key design patterns and architectural paradigm.

## 2. Architecture & System Topology
```mermaid
graph TD
    %% Component architecture diagram
```
- Narrative explanation of subsystem boundaries and interactions.

## 3. Directory Layout & Module Decomposition
- Breakdown of critical directories and modules with concise functional responsibilities.

## 4. Core Features & Code Walkthrough
- Deep dive into standout mechanisms, core algorithms, data processing, or calculations.
- File and symbol references (use clickable markdown links).

## 5. Data Flow & State Management
- How data enters the system, flows through components, transforms, and persists.

## 6. Public & External Interfaces
- APIs, CLI commands, IPC channels, WebSocket protocols, or native bridges.

## 7. Findings & Evidence Ledger
- **Direct Observations (Facts)**: Verified behaviors backed by code / artifacts.
- **Architectural Inferences (Hypotheses)**: Logical deductions.
- **Unknowns & Technical Debt**: Hidden areas, security risks, missing documentation, or external dependencies.

## 8. Reconstruction / Integration Guide
- Actionable steps, recipes, or pseudocode for replicating, adapting, or integrating the analyzed features into our project.
```

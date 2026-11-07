# AI Skills Bundle

A collection of 247 skills and example rules for Claude Code, Codex and similar AI agents. It contains no API keys, account IDs or private data.

## Quick install

Send this to your AI:

```text
https://raw.githubusercontent.com/serdevir91/ai-skills-bundle/main/INSTALL.md
Install the skills using the instructions in this file.
```

Manual install:

```bash
git clone --depth 1 https://github.com/serdevir91/ai-skills-bundle.git
cd ai-skills-bundle
./install.sh --list
./install.sh custom workflow
```

The default target is `~/.claude/skills`. Use `--target DIR` for another folder. Install only the groups you need, because every skill adds to the agent's context.

The zip is also available: [ai-skills-bundle.zip](https://github.com/serdevir91/ai-skills-bundle/releases/download/v1.0.0/ai-skills-bundle.zip)

## Contents

| Folder | Skills | Contents |
|---|---:|---|
| [`skills/custom/`](#custom-11) | 11 | Store publishing, Flutter baseline and audit, agent delegation, scraping, reverse engineering |
| [`skills/workflow/`](#workflow-22) | 22 | Terse replies, careful coding, review and verification flows |
| [`skills/firebase/`](#firebase-13) | 13 | Firebase, Firestore and Xcode setup |
| [`skills/anthropic/`](#anthropic-13) | 13 | Design, documents, MCP and testing |
| [`skills/community/`](#community-188) | 188 | Engineering, product, marketing, leadership and compliance roles |
| `rules/` | | Example `AGENTS.md` and `CLAUDE.md` rules |
| `scripts/` | | Hooks that shut down idle iOS Simulators |

`brand-guidelines` exists in both `anthropic` and `community`, so installing everything gives 246 unique skills.

Values such as `<ISSUER_ID>`, `<KEY_ID>`, `<WORKSPACE>` and `com.example.myapp` are placeholders. Replace them with your own.

## Not included

- Anthropic `docx`, `pdf`, `pptx` and `xlsx`: their licences do not allow redistribution. Source: https://github.com/anthropics/skills
- `upload_to_*.py` store scripts and personal notes. The publish skills need your own versions of these scripts.

## Install separately

- Plugins: `JuliusBrussee/caveman`, `Creatorberry/flick`
- Delegation CLIs: Antigravity (`agy`), OpenCode (`opencode`)
- Scraping: `scrapling`

## Skill catalog

### Custom (11)

Publishing, Flutter, delegation, scraping and reverse engineering. Install with `./install.sh custom`.

| Skill | What it does |
|---|---|
| [`antigravity-delegate`](skills/custom/antigravity-delegate/) | Hand a coding or ops task to the Antigravity CLI (`agy`), fall back to another model on limits, then check the result. |
| [`app-store-publish`](skills/custom/app-store-publish/) | Build iOS apps, upload to TestFlight and manage App Store Connect with an API key and your own `upload_to_appstore.py`. |
| [`crew-delegate`](skills/custom/crew-delegate/) | Boss/worker flow: the main AI plans and verifies while Antigravity and OpenCode CLIs do delegated coding. |
| [`flutter-feature-audit`](skills/custom/flutter-feature-audit/) | Audit one or many Flutter apps for theme support, update checks and in-app review before release. |
| [`flutter-feature-baseline`](skills/custom/flutter-feature-baseline/) | Add a standard Flutter baseline: light/dark/AMOLED themes, update checks, in-app review and purchases. |
| [`hermes-delegate`](skills/custom/hermes-delegate/) | Offload long jobs, scraping or batch work to a remote server reached through the SSH alias `hermes`. |
| [`msstore-publish`](skills/custom/msstore-publish/) | Build MSIX packages and publish Flutter or Windows apps to the Microsoft Store with your own `upload_to_msstore.py`. |
| [`play-store-publish`](skills/custom/play-store-publish/) | Build AABs, upload to Google Play and manage listings and products with your own `upload_to_playstore.py`. |
| [`reverse-engineer-anything`](skills/custom/reverse-engineer-anything/) | Inspect and report on any repository or compiled app: native binaries, APKs, Electron/ASAR, .NET and web runtimes. |
| [`scrapling-official`](skills/custom/scrapling-official/) | Scrape pages with Scrapling: HTTP requests, stealth browsers, JavaScript rendering, spiders and adaptive parsing. |
| [`xcross-flutter-ios`](skills/custom/xcross-flutter-ios/) | Build, run and debug Flutter iOS apps from Windows or Linux with xcross, without a Mac or Xcode. |

### Workflow (22)

Terse replies, careful coding and review flows, mostly from Caveman. Install with `./install.sh workflow`.

| Skill | What it does |
|---|---|
| [`cavecrew`](skills/workflow/cavecrew/) | Decide when to delegate to the Caveman investigator, builder or reviewer subagents. |
| [`caveman`](skills/workflow/caveman/) | Terse reply mode: answer first, drop filler, keep every technical fact. Cuts output tokens. |
| [`caveman-commit`](skills/workflow/caveman-commit/) | Write compressed Conventional Commits messages. |
| [`caveman-compress`](skills/workflow/caveman-compress/) | Compress memory files such as `CLAUDE.md` to save input tokens, keeping a readable backup. |
| [`caveman-discover`](skills/workflow/caveman-discover/) | Find and label LLM workflows in a repository so Caveman Cloud can group spend by workflow. |
| [`caveman-evidence-review`](skills/workflow/caveman-evidence-review/) | Read-only review of Caveman Cloud cost, latency, errors, routing and savings data. |
| [`caveman-explore`](skills/workflow/caveman-explore/) | Read-only repository explorer that returns `path:line` citations. |
| [`caveman-help`](skills/workflow/caveman-help/) | Quick-reference card for the Caveman skills and commands. |
| [`caveman-learn`](skills/workflow/caveman-learn/) | Review ranked token sinks from a Caveman report and apply cost-lowering fixes with consent. |
| [`caveman-manage`](skills/workflow/caveman-manage/) | Inspect the Caveman Cloud experiment lifecycle and block unsafe execution. |
| [`caveman-optimize`](skills/workflow/caveman-optimize/) | Turn a Caveman optimization observation into a candidate with a paired baseline evaluation. |
| [`caveman-review`](skills/workflow/caveman-review/) | Compressed code review: one line per finding with location, problem and fix. |
| [`caveman-setup`](skills/workflow/caveman-setup/) | Route a repository through the Caveman Cloud gateway to measure every LLM request. |
| [`caveman-stats`](skills/workflow/caveman-stats/) | Show token usage and mode attribution for the current Claude Code session. |
| [`investigate-first`](skills/workflow/investigate-first/) | Diagnose unclear failures and rank hypotheses with evidence before editing code. |
| [`lean-build`](skills/workflow/lean-build/) | Build features with strict scope, code reuse and an explicit stop condition to avoid overbuilding. |
| [`megacave`](skills/workflow/megacave/) | Caveman mode in Classical Chinese register for far fewer characters. |
| [`migration`](skills/workflow/migration/) | Implement reversible schema, data, API or dependency migrations with rollback proof. |
| [`safe-refactor`](skills/workflow/safe-refactor/) | Restructure code without changing behavior, with verification before and after the edits. |
| [`surgical-patch`](skills/workflow/surgical-patch/) | Fix bugs at the narrowest responsible layer with regression proof. |
| [`ultracave`](skills/workflow/ultracave/) | Caveman mode at maximum compression. |
| [`verify-and-stop`](skills/workflow/verify-and-stop/) | Prove existing work meets its acceptance conditions without expanding scope. |

### Firebase (13)

Firebase, Firestore and Xcode setup. Install with `./install.sh firebase`.

| Skill | What it does |
|---|---|
| [`extension-to-functions-codebase`](skills/firebase/extension-to-functions-codebase/) | Convert an installed Firebase Extension into a standalone Cloud Functions codebase or npm package. |
| [`firebase-ai-logic-basics`](skills/firebase/firebase-ai-logic-basics/) | Call Gemini models from Android, iOS, Web and Flutter clients with Firebase AI Logic. |
| [`firebase-app-hosting-basics`](skills/firebase/firebase-app-hosting-basics/) | Deploy full-stack Next.js and Angular apps with SSR on Firebase App Hosting. |
| [`firebase-auth-basics`](skills/firebase/firebase-auth-basics/) | Set up Firebase Authentication, user management and auth-based security rules. |
| [`firebase-basics`](skills/firebase/firebase-basics/) | Install and log in to the Firebase CLI, create projects and set up the core tooling. |
| [`firebase-crashlytics`](skills/firebase/firebase-crashlytics/) | Set up Firebase Crashlytics and crash reporting in an app. |
| [`firebase-data-connect`](skills/firebase/firebase-data-connect/) | Build and deploy Firebase SQL Connect (Data Connect) backends on PostgreSQL. |
| [`firebase-firestore`](skills/firebase/firebase-firestore/) | Set up and query Cloud Firestore: data modeling, security rules, indexes and SDKs. |
| [`firebase-hosting-basics`](skills/firebase/firebase-hosting-basics/) | Deploy static sites and SPAs on classic Firebase Hosting with custom domains. |
| [`firebase-remote-config-basics`](skills/firebase/firebase-remote-config-basics/) | Manage Remote Config templates, feature flags and SDK loading strategies. |
| [`firebase-security-rules-auditor`](skills/firebase/firebase-security-rules-auditor/) | Audit Firestore and Cloud Storage rules for vulnerabilities and privilege escalation. |
| [`firestore-rules-creation`](skills/firebase/firestore-rules-creation/) | Design and harden production Cloud Firestore security rules. |
| [`xcode-project-setup`](skills/firebase/xcode-project-setup/) | Safely edit Xcode projects (`.pbxproj`) to add Swift Packages and link files. |

### Anthropic (13)

Design, documents, MCP and testing. Install with `./install.sh anthropic`.

| Skill | What it does |
|---|---|
| [`algorithmic-art`](skills/anthropic/algorithmic-art/) | Create generative art with p5.js, seeded randomness and interactive parameters. |
| [`brand-guidelines`](skills/anthropic/brand-guidelines/) | Apply Anthropic's brand colors and typography to an artifact. |
| [`canvas-design`](skills/anthropic/canvas-design/) | Create posters and visual art as `.png` and `.pdf` files. |
| [`claude-api`](skills/anthropic/claude-api/) | Build apps with the Claude API and Anthropic SDKs. |
| [`doc-coauthoring`](skills/anthropic/doc-coauthoring/) | Structured workflow for co-writing docs, proposals, specs and decision records. |
| [`frontend-design`](skills/anthropic/frontend-design/) | Build distinctive, production-grade frontend interfaces. |
| [`internal-comms`](skills/anthropic/internal-comms/) | Write internal communications in common company formats. |
| [`mcp-builder`](skills/anthropic/mcp-builder/) | Create high-quality MCP servers that connect LLMs to external services. |
| [`skill-creator`](skills/anthropic/skill-creator/) | Create, improve and measure skills, including evals and description tuning. |
| [`slack-gif-creator`](skills/anthropic/slack-gif-creator/) | Create animated GIFs optimized for Slack. |
| [`theme-factory`](skills/anthropic/theme-factory/) | Style slides, docs and pages with 10 preset color and font themes, or a custom one. |
| [`web-artifacts-builder`](skills/anthropic/web-artifacts-builder/) | Build complex multi-component HTML artifacts with React, Tailwind and shadcn/ui. |
| [`webapp-testing`](skills/anthropic/webapp-testing/) | Test local web apps with Playwright: UI checks, debugging and screenshots. |

### Community (188)

Role-based skills for engineering, product, marketing, leadership and compliance. Install with `./install.sh community`.

#### AI agents and LLM engineering (19)

| Skill | What it does |
|---|---|
| [`agent-designer`](skills/community/agent-designer/) | Design multi-agent systems (supervisor, swarm, pipeline) and tool schemas; find bottlenecks in run logs. |
| [`agent-handoff`](skills/community/agent-handoff/) | Keep a central `agent.md` knowledge file to pass context between AI sessions. |
| [`agent-protocol`](skills/community/agent-protocol/) | Let C-suite advisor agents call each other or run multi-role meetings. |
| [`agent-workflow-designer`](skills/community/agent-workflow-designer/) | Design multi-agent workflows with handoff contracts, failure handling and cost controls. |
| [`agenthub`](skills/community/agenthub/) | Run several agents on one task in parallel and keep the best result: faster code, copy variants, research angles. |
| [`autoresearch-agent`](skills/community/autoresearch-agent/) | Make a file measurably better by trial: faster code, smaller bundle, higher pass rate or prompt score. |
| [`context-engine`](skills/community/context-engine/) | Starting a C-suite advisor session, when company context is missing or older than 90 days, or before company data goes to an external service. |
| [`llm-cost-optimizer`](skills/community/llm-cost-optimizer/) | Cut LLM API spend with model routing, prompt caching and cost observability. |
| [`mcp-server-builder`](skills/community/mcp-server-builder/) | Build MCP servers from API contracts. |
| [`prompt-engineer-toolkit`](skills/community/prompt-engineer-toolkit/) | Analyze and rewrite prompts and create reusable prompt templates. |
| [`prompt-governance`](skills/community/prompt-governance/) | Manage production prompts: versioning, A/B tests, registries and regression checks. |
| [`rag-architect`](skills/community/rag-architect/) | Design a RAG pipeline: chunk size, embedding model, vector database and retrieval quality metrics. |
| [`self-eval`](skills/community/self-eval/) | Grade finished work honestly on two axes with a devil's-advocate pass against inflation. |
| [`self-improving-agent`](skills/community/self-improving-agent/) | Curate Claude Code's auto-memory into durable project knowledge. |
| [`senior-computer-vision`](skills/community/senior-computer-vision/) | Build and deploy object detection and segmentation models. |
| [`senior-ml-engineer`](skills/community/senior-ml-engineer/) | Putting ML models or LLM features into production: deployment, MLOps, drift monitoring, RAG pipelines, LLM API cost and retries. |
| [`senior-prompt-engineer`](skills/community/senior-prompt-engineer/) | Optimize prompts, design templates and evaluate LLM outputs. |
| [`skill-security-auditor`](skills/community/skill-security-auditor/) | Audit a skill or plugin from an untrusted source before installing it. |
| [`skill-tester`](skills/community/skill-tester/) | Validate, test and score skill quality. |

#### Software engineering (34)

| Skill | What it does |
|---|---|
| [`a11y-audit`](skills/community/a11y-audit/) | Scan, fix and verify WCAG 2.2 A/AA accessibility across major frontend frameworks. |
| [`adversarial-reviewer`](skills/community/adversarial-reviewer/) | Tough, critical review of a diff or PR before merge, through hostile reviewer personas that catch shared blind spots. |
| [`api-design-reviewer`](skills/community/api-design-reviewer/) | Review API designs against REST conventions and best practices. |
| [`api-test-suite-builder`](skills/community/api-test-suite-builder/) | Asked to write API, integration or contract tests for REST endpoints. |
| [`browser-automation`](skills/community/browser-automation/) | Automate a browser: scrape websites, fill forms, pull structured data from web pages. |
| [`changelog-generator`](skills/community/changelog-generator/) | Generate release notes from Conventional Commits. |
| [`code-reviewer`](skills/community/code-reviewer/) | Automated code review for TypeScript, JavaScript, Python, Go, Swift and Kotlin. |
| [`code-to-prd`](skills/community/code-to-prd/) | Asked to write a PRD or product spec from an existing codebase (reverse-engineer requirements, document pages, fields, routes and endpoints). |
| [`codebase-onboarding`](skills/community/codebase-onboarding/) | Analyze a codebase and generate onboarding docs for new developers. |
| [`database-designer`](skills/community/database-designer/) | Design a database schema: tables, relationships, indexes, normalization, SQL vs NoSQL, migration plans. |
| [`database-schema-designer`](skills/community/database-schema-designer/) | Asked for an ERD, table relationships, normalization or a schema migration plan. |
| [`dependency-auditor`](skills/community/dependency-auditor/) | Analyze and audit dependencies across multi-language projects. |
| [`focused-fix`](skills/community/focused-fix/) | A whole feature or module is broken and needs fixing end to end ('make X work', 'the Y module is broken'). |
| [`git-worktree-manager`](skills/community/git-worktree-manager/) | Run parallel feature work with isolated Git worktrees, ports and environments. |
| [`migration-architect`](skills/community/migration-architect/) | Plan, execute and validate complex system migrations with minimal business impact. |
| [`monorepo-navigator`](skills/community/monorepo-navigator/) | Manage Turborepo, Nx, pnpm workspace and Lerna monorepos. |
| [`performance-profiler`](skills/community/performance-profiler/) | Profile Node.js, Python and Go apps for CPU, memory and I/O bottlenecks. |
| [`playwright-pro`](skills/community/playwright-pro/) | Write, fix and migrate Playwright tests, with CI, TestRail and BrowserStack support. |
| [`pr-review-expert`](skills/community/pr-review-expert/) | File-by-file pull request review for bugs, security and quality, with a merge verdict. |
| [`saas-scaffolder`](skills/community/saas-scaffolder/) | Generate SaaS boilerplate with auth, database, billing and API routes. |
| [`senior-architect`](skills/community/senior-architect/) | Design system architecture and compare microservices with monoliths. |
| [`senior-backend`](skills/community/senior-backend/) | Build and fix backend services: REST or GraphQL APIs, auth, microservices, PostgreSQL queries, migrations and load tests. |
| [`senior-data-engineer`](skills/community/senior-data-engineer/) | Data pipelines: Airflow DAGs, Spark, dbt, Kafka, ETL/ELT, data quality checks. |
| [`senior-data-scientist`](skills/community/senior-data-scientist/) | Design experiments and analyze tabular data: A/B tests, causal inference, feature engineering, model evaluation. |
| [`senior-frontend`](skills/community/senior-frontend/) | Build and review React, Next.js, TypeScript or Tailwind frontends: components, scaffolding, performance and bundle size. |
| [`senior-fullstack`](skills/community/senior-fullstack/) | Scaffold Next.js, FastAPI, MERN and Django projects and analyze code quality. |
| [`senior-qa`](skills/community/senior-qa/) | Write and improve tests for React or Next.js apps: Jest, React Testing Library, MSW mocks, Playwright E2E, coverage gaps. |
| [`snowflake-development`](skills/community/snowflake-development/) | Write Snowflake SQL, build pipelines and use Cortex AI functions. |
| [`spec-driven-workflow`](skills/community/spec-driven-workflow/) | Write specs and acceptance criteria before code, then generate tests from them. |
| [`sql-database-assistant`](skills/community/sql-database-assistant/) | Write and optimize SQL, generate migrations and work with ORMs. |
| [`stripe-integration-expert`](skills/community/stripe-integration-expert/) | Implement Stripe subscriptions, one-time payments, usage billing and checkout. |
| [`tdd-guide`](skills/community/tdd-guide/) | Guide test-driven development: unit tests, fixtures, mocks and coverage gaps. |
| [`tech-debt-tracker`](skills/community/tech-debt-tracker/) | Find, rank and track tech debt in a codebase. |
| [`tech-stack-evaluator`](skills/community/tech-stack-evaluator/) | Compare frameworks or tech stacks before committing: side-by-side scoring, total cost of ownership, ecosystem health and migration risk. |

#### Cloud, DevOps and IT admin (15)

| Skill | What it does |
|---|---|
| [`aws-solution-architect`](skills/community/aws-solution-architect/) | Designing or costing an AWS architecture (serverless, Lambda, API Gateway, DynamoDB, ECS, Aurora, CloudFormation, migration to AWS). |
| [`azure-cloud-architect`](skills/community/azure-cloud-architect/) | Designing or costing an Azure architecture (AKS, App Service, Functions, Cosmos DB, Bicep or ARM, Azure DevOps, migration to Azure). |
| [`ci-cd-pipeline-builder`](skills/community/ci-cd-pipeline-builder/) | Generate CI/CD pipelines from detected project stack signals. |
| [`docker-development`](skills/community/docker-development/) | Optimize Dockerfiles, compose setups, multi-stage builds and container security. |
| [`env-secrets-manager`](skills/community/env-secrets-manager/) | Audit environment variable hygiene, secrets safety and rotation readiness. |
| [`gcp-cloud-architect`](skills/community/gcp-cloud-architect/) | Design, deploy and cut the cost of Google Cloud setups: Cloud Run, GKE, Functions, Cloud SQL, BigQuery, moving to GCP. |
| [`google-workspace-cli`](skills/community/google-workspace-cli/) | Google Workspace admin or automation from the gws CLI (Gmail, Drive, Sheets, Calendar, Docs, Chat, Tasks). |
| [`helm-chart-builder`](skills/community/helm-chart-builder/) | Scaffold and review Helm charts, values and templates. |
| [`incident-commander`](skills/community/incident-commander/) | Manage technology incidents from detection through resolution. |
| [`ms365-tenant-manager`](skills/community/ms365-tenant-manager/) | Microsoft 365 tenant administration (Entra ID users, Exchange Online, Teams, licenses, Conditional Access, compliance reports). |
| [`observability-designer`](skills/community/observability-designer/) | Design observability strategies, including SLI/SLO/SLA frameworks. |
| [`runbook-generator`](skills/community/runbook-generator/) | Generate operational runbooks for deployment, incidents, maintenance and rollback. |
| [`secrets-vault-manager`](skills/community/secrets-vault-manager/) | Set up HashiCorp Vault and AWS, Azure or GCP secret stores. |
| [`senior-devops`](skills/community/senior-devops/) | Set up CI/CD pipelines, infrastructure as code, containers and deployments on AWS, GCP or Azure. |
| [`terraform-patterns`](skills/community/terraform-patterns/) | Terraform module design, state management, provider configuration and security hardening. |

#### Security (8)

| Skill | What it does |
|---|---|
| [`ai-security`](skills/community/ai-security/) | Assess AI/ML systems for prompt injection, jailbreaks, data poisoning and tool abuse. |
| [`cloud-security`](skills/community/cloud-security/) | Assess cloud setups for misconfigurations, IAM escalation paths and public exposure. |
| [`incident-response`](skills/community/incident-response/) | Triage a security incident: classification, escalation and forensic evidence. |
| [`red-team`](skills/community/red-team/) | Plan authorized red team engagements and attack path analysis. |
| [`security-pen-testing`](skills/community/security-pen-testing/) | Run authorized security audits, vulnerability scans and OWASP Top 10 checks. |
| [`senior-secops`](skills/community/senior-secops/) | Find and fix application security problems: security reviews, CVE remediation, hardening, secrets and auth, SOC 2, PCI-DSS, HIPAA and GDPR checks. |
| [`senior-security`](skills/community/senior-security/) | Check if a design or code is secure: STRIDE threat model, DREAD risk scores, leaked secret scan. |
| [`threat-detection`](skills/community/threat-detection/) | Hunt for threats, analyze IOCs and detect anomalies in telemetry. |

#### Product, design and project management (18)

| Skill | What it does |
|---|---|
| [`agile-product-owner`](skills/community/agile-product-owner/) | Backlog work: writing user stories and acceptance criteria, splitting epics, estimating or prioritizing for a sprint. |
| [`atlassian-admin`](skills/community/atlassian-admin/) | Administer Jira, Confluence, Bitbucket and Trello: users, permissions and security. |
| [`atlassian-templates`](skills/community/atlassian-templates/) | Create and manage Jira and Confluence templates, blueprints and layouts. |
| [`confluence-expert`](skills/community/confluence-expert/) | Building or restructuring a Confluence space: page hierarchy, permissions, templates, Jira macros or a content audit. |
| [`epic-design`](skills/community/epic-design/) | Build cinematic 2.5D websites with scroll storytelling and parallax depth. |
| [`experiment-designer`](skills/community/experiment-designer/) | Plan product experiments, testable hypotheses and sample sizes, and read A/B outcomes. |
| [`jira-expert`](skills/community/jira-expert/) | Manage Jira projects, JQL, workflows, custom fields, automation and reporting. |
| [`meeting-analyzer`](skills/community/meeting-analyzer/) | Analyze meeting transcripts for communication patterns and coaching feedback. |
| [`product-analytics`](skills/community/product-analytics/) | Define KPIs, dashboards, and cohort, retention and feature adoption analysis. |
| [`product-discovery`](skills/community/product-discovery/) | Validate opportunities, map assumptions and test problem-solution fit. |
| [`product-manager-toolkit`](skills/community/product-manager-toolkit/) | RICE prioritization, interview analysis, PRD templates and discovery frameworks. |
| [`product-strategist`](skills/community/product-strategist/) | OKR cascades, quarterly planning and competitive analysis for product leaders. |
| [`research-summarizer`](skills/community/research-summarizer/) | Summarizing a research paper, article or report, comparing several sources or extracting citations into a brief. |
| [`roadmap-communicator`](skills/community/roadmap-communicator/) | Prepare roadmap narratives, release notes and stakeholder updates. |
| [`scrum-master`](skills/community/scrum-master/) | Sprint and team analytics: velocity forecasts, sprint health, retrospectives, burndown or blockers. |
| [`senior-pm`](skills/community/senior-pm/) | Project and portfolio management for multi-workstream programs: plans, status reports, risk registers, capacity, executive reporting. |
| [`ui-design-system`](skills/community/ui-design-system/) | Generate design tokens, component docs and responsive design calculations. |
| [`ux-researcher-designer`](skills/community/ux-researcher-designer/) | Create personas, journey maps and usability test plans. |

#### Marketing, SEO and growth (46)

| Skill | What it does |
|---|---|
| [`ab-test-setup`](skills/community/ab-test-setup/) | Use before planning or launching any A/B, split or multivariate test, or when asked if a result is significant. |
| [`ad-creative`](skills/community/ad-creative/) | Write ad copy and bulk variations for Google, Meta, LinkedIn and TikTok. |
| [`aeo`](skills/community/aeo/) | Answer engine optimization: score content and rewrite it so ChatGPT, Perplexity, Claude and Gemini cite it. |
| [`analytics-tracking`](skills/community/analytics-tracking/) | Any GA4, Google Tag Manager, event-tracking or conversion-tracking setup, audit or broken-event debug, before touching tags. |
| [`app-store-optimization`](skills/community/app-store-optimization/) | App Store Optimization: keyword research, competitor rankings and metadata suggestions. |
| [`brand-guidelines`](skills/community/brand-guidelines/) | Apply, document or enforce brand guidelines for any product or company. |
| [`campaign-analytics`](skills/community/campaign-analytics/) | Analyze campaign performance on the user's numbers: ROAS, CPA, ROI, multi-touch attribution and funnel drop-off. |
| [`churn-prevention`](skills/community/churn-prevention/) | Designing a cancel flow, save offers, exit surveys or dunning emails, or cutting failed-payment churn. |
| [`cold-email`](skills/community/cold-email/) | Any cold outreach or SDR email or follow-up sequence to prospects who did not opt in, before drafting. |
| [`competitive-teardown`](skills/community/competitive-teardown/) | Analyze competitors from pricing pages, reviews, job posts, SEO and social signals. |
| [`competitor-alternatives`](skills/community/competitor-alternatives/) | Creating an 'X vs Y', '[product] alternative' or comparison page, before drafting. |
| [`content-creator`](skills/community/content-creator/) | Deprecated redirect that routes old content requests to the right specialist skill. |
| [`content-humanizer`](skills/community/content-humanizer/) | Make a draft sound less like AI: fix generic, robotic text with rhythm, specifics, personality and brand voice. |
| [`content-production`](skills/community/content-production/) | Write a blog post, article or guide end to end: research, outline, draft, SEO pass and quality gates. |
| [`content-strategy`](skills/community/content-strategy/) | Deciding what content to create (topics, clusters, a blog or content plan), before listing ideas. |
| [`copy-editing`](skills/community/copy-editing/) | Edit, proofread and tighten existing marketing copy in focused passes: clarity, voice, proofreading, specificity, readability and AI tells. |
| [`copywriting`](skills/community/copywriting/) | Write or improve marketing copy for any page. |
| [`email-sequence`](skills/community/email-sequence/) | Any drip, nurture, onboarding, welcome or re-engagement email sequence to opted-in users, before writing emails. |
| [`email-template-builder`](skills/community/email-template-builder/) | Build transactional email systems with React Email templates and provider integration. |
| [`form-cro`](skills/community/form-cro/) | Optimize lead capture, contact, demo and survey forms for conversion. |
| [`free-tool-strategy`](skills/community/free-tool-strategy/) | Considering a free calculator, grader, checker or generator as a marketing asset, before building it. |
| [`landing-page-generator`](skills/community/landing-page-generator/) | Asked for a landing, marketing or campaign page as a Next.js TSX component with Tailwind. |
| [`launch-strategy`](skills/community/launch-strategy/) | Plan a product or feature launch: readiness score and a phased plan by channel. |
| [`marketing-context`](skills/community/marketing-context/) | Capture ICP, positioning and brand voice before other marketing skills run. |
| [`marketing-demand-acquisition`](skills/community/marketing-demand-acquisition/) | Plan demand generation, paid spend, SEO and partnership campaigns. |
| [`marketing-ideas`](skills/community/marketing-ideas/) | Generate marketing ideas and strategies for SaaS products. |
| [`marketing-ops`](skills/community/marketing-ops/) | A marketing request spans several skills (a campaign across content, SEO, CRO and channels) or it is unclear which skill fits. |
| [`marketing-psychology`](skills/community/marketing-psychology/) | Apply persuasion and behavioral science ethically to a page, offer or campaign, from 70+ mental models. |
| [`marketing-strategy-pmm`](skills/community/marketing-strategy-pmm/) | Product positioning, ICP, competitive battlecards or a go-to-market plan, before drafting. |
| [`onboarding-cro`](skills/community/onboarding-cro/) | Activation, time-to-value or a first-run experience after signup needs work, before redesigning it. |
| [`page-cro`](skills/community/page-cro/) | Fix a page that is not converting: section by section audit with fixes ranked by impact. |
| [`paid-ads`](skills/community/paid-ads/) | Plan and optimize campaigns on Google, Meta, LinkedIn and X. |
| [`paywall-upgrade-cro`](skills/community/paywall-upgrade-cro/) | Designing or fixing an in-app paywall, upgrade modal, feature gate or trial-expiry screen. |
| [`popup-cro`](skills/community/popup-cro/) | Creating or fixing a popup, modal, exit-intent, slide-in or banner meant to convert. |
| [`pricing-strategy`](skills/community/pricing-strategy/) | SaaS pricing tiers, value metric, packaging, a pricing page or a price increase, before proposing numbers. |
| [`programmatic-seo`](skills/community/programmatic-seo/) | Building many SEO pages from a template and data (location, integration, comparison or directory pages), before generating them. |
| [`referral-program`](skills/community/referral-program/) | Designing or fixing a referral, affiliate or ambassador program, before setting rewards. |
| [`schema-markup`](skills/community/schema-markup/) | Implement, audit and validate structured data on a website. |
| [`seo-audit`](skills/community/seo-audit/) | Audit and diagnose SEO issues on a site. |
| [`signup-flow-cro`](skills/community/signup-flow-cro/) | Signup, registration or trial-start conversion is low or a signup flow is being designed. |
| [`site-architecture`](skills/community/site-architecture/) | Plan website structure, URL hierarchy, navigation and internal linking. |
| [`social-content`](skills/community/social-content/) | Create and schedule content for LinkedIn, X, Instagram, TikTok and Facebook. |
| [`social-media-analyzer`](skills/community/social-media-analyzer/) | Score social performance: engagement rate, reach, ROI per platform, benchmarks. |
| [`social-media-manager`](skills/community/social-media-manager/) | Plan social strategy, content calendars and community engagement. |
| [`video-content-strategist`](skills/community/video-content-strategist/) | Plan video strategy, scripts, YouTube growth and short-form pipelines. |
| [`x-twitter-growth`](skills/community/x-twitter-growth/) | Growing on X/Twitter: tweets, threads, profile audit, competitors or posting plan. |

#### Leadership, business and operations (35)

| Skill | What it does |
|---|---|
| [`board-deck-builder`](skills/community/board-deck-builder/) | Building a board deck, investor update or QBR from all C-suite perspectives. |
| [`board-meeting`](skills/community/board-meeting/) | Run a structured multi-executive deliberation on a strategic question. |
| [`business-investment-advisor`](skills/community/business-investment-advisor/) | Analyze capital spending with ROI, IRR, NPV and payback. |
| [`ceo-advisor`](skills/community/ceo-advisor/) | Advice for a CEO or founder on running the company: board and investor trouble, raise or cut, strategy bets, org and culture. |
| [`cfo-advisor`](skills/community/cfo-advisor/) | Startup finance: runway and burn, unit economics (LTV, CAC, payback), fundraising and dilution. |
| [`change-management`](skills/community/change-management/) | Rolling out a reorg, pivot, tool switch, leadership change or product kill. |
| [`chief-of-staff`](skills/community/chief-of-staff/) | Orchestrate and route work across the C-suite advisor skills. |
| [`chro-advisor`](skills/community/chro-advisor/) | People strategy: hiring plans, comp bands, org structure, performance, retention. |
| [`ciso-advisor`](skills/community/ciso-advisor/) | Security leadership decisions: a security program, budget justification in dollars, SOC 2 vs ISO 27001 vs HIPAA roadmap, or board security reporting. |
| [`cmo-advisor`](skills/community/cmo-advisor/) | Marketing leadership: positioning, product-led vs sales-led vs community-led growth, budget split across channels, marketing team design. |
| [`company-os`](skills/community/company-os/) | Choosing or setting up how the company runs: EOS, Scaling Up or OKRs, accountability chart, scorecard, meeting rhythm, quarterly rocks. |
| [`competitive-intel`](skills/community/competitive-intel/) | Competitor analysis, battlecards, win/loss review or positioning against alternatives. |
| [`contract-and-proposal-writer`](skills/community/contract-and-proposal-writer/) | Draft contracts, proposals, SOWs, NDAs and MSAs for several jurisdictions. |
| [`coo-advisor`](skills/community/coo-advisor/) | Operations leadership: process design, OKR execution, operating cadence, bottlenecks or scaling playbooks. |
| [`cpo-advisor`](skills/community/cpo-advisor/) | Product leadership: PMF measurement, product vision, portfolio investment, product org design, board product reporting. |
| [`cro-advisor`](skills/community/cro-advisor/) | B2B revenue leadership: forecasting, quotas, sales model, NRR and churn, pricing or sales capacity. |
| [`cs-onboard`](skills/community/cs-onboard/) | Setting up the C-suite advisors for the first time, or when company context is missing or stale after a raise or pivot. |
| [`cto-advisor`](skills/community/cto-advisor/) | CTO decisions: tech debt, architecture direction, scaling the engineering team, technology evaluation, DORA metrics. |
| [`culture-architect`](skills/community/culture-architect/) | Defining company values, turning them into behaviors, assessing culture health or designing rituals. |
| [`customer-success-manager`](skills/community/customer-success-manager/) | Reviewing customer accounts for health, churn risk or expansion. |
| [`decision-logger`](skills/community/decision-logger/) | Logging a decision after a board meeting, reviewing past decisions or checking overdue actions. |
| [`executive-mentor`](skills/community/executive-mentor/) | A founder or executive needs a plan stress-tested, a dreaded decision made, a hard board meeting prepared or an honest post-mortem. |
| [`financial-analyst`](skills/community/financial-analyst/) | Analyze financial statements, value a company with a DCF, explain budget variance, build rolling forecasts. |
| [`founder-coach`](skills/community/founder-coach/) | Coach founders through delegation, burnout and the move from IC to CEO. |
| [`internal-narrative`](skills/community/internal-narrative/) | Preparing an all-hands, investor update, recruiting pitch or crisis message, or when stories told to different audiences drift apart. |
| [`interview-system-designer`](skills/community/interview-system-designer/) | Design hiring pipelines, interview loops and calibration. |
| [`intl-expansion`](skills/community/intl-expansion/) | Expanding to a new country: market selection, entry mode, localization, regulation and regional go-to-market. |
| [`ma-playbook`](skills/community/ma-playbook/) | Buy a company or sell yours: diligence, valuation, terms, integration. |
| [`org-health-diagnostic`](skills/community/org-health-diagnostic/) | A whole-company health check before a board review or when functions seem at risk. |
| [`revenue-operations`](skills/community/revenue-operations/) | Check sales pipeline and forecasts: pipeline coverage, forecast accuracy, magic number, CAC payback. |
| [`saas-metrics-coach`](skills/community/saas-metrics-coach/) | Interpret SaaS numbers such as ARR, MRR, churn, LTV, CAC and NRR. |
| [`sales-engineer`](skills/community/sales-engineer/) | Analyze RFP gaps, build feature comparison matrices and plan POCs. |
| [`scenario-war-room`](skills/community/scenario-war-room/) | Compound what-if questions ('what if X and Y both happen?') with major downside across functions. |
| [`strategic-alignment`](skills/community/strategic-alignment/) | Teams pull in different directions, OKRs don't connect or departments optimize locally. |
| [`team-communications`](skills/community/team-communications/) | Write 3P updates, newsletters, FAQ roundups and incident reports. |

#### Compliance and quality (13)

| Skill | What it does |
|---|---|
| [`capa-officer`](skills/community/capa-officer/) | CAPA work in a medical device QMS: root cause analysis (5-Why, fishbone), corrective action plans, effectiveness checks or CAPA metrics. |
| [`fda-consultant-specialist`](skills/community/fda-consultant-specialist/) | FDA medical device questions: 510(k) vs De Novo vs PMA, predicates and substantial equivalence, QMSR (21 CFR 820), HIPAA or device cybersecurity. |
| [`gdpr-dsgvo-expert`](skills/community/gdpr-dsgvo-expert/) | GDPR or DSGVO work: scanning a codebase for privacy risks, writing a DPIA or tracking data subject requests against the Art. 12(3) deadline. |
| [`information-security-manager-iso27001`](skills/community/information-security-manager-iso27001/) | Design and run an ISO 27001 ISMS for HealthTech and MedTech companies. |
| [`isms-audit-expert`](skills/community/isms-audit-expert/) | Audit an ISO 27001 ISMS: controls, compliance checks and certification prep. |
| [`mdr-745-specialist`](skills/community/mdr-745-specialist/) | EU MDR 2017/745 work: classification, technical files, clinical evaluation and PMS. |
| [`qms-audit-expert`](skills/community/qms-audit-expert/) | ISO 13485 internal audits: planning the program, running an audit, classifying findings or preparing for an external audit. |
| [`quality-documentation-manager`](skills/community/quality-documentation-manager/) | QMS document control: numbering, versioning, change control or 21 CFR Part 11 e-signatures. |
| [`quality-manager-qmr`](skills/community/quality-manager-qmr/) | QMR duties under ISO 13485 5.5.2: management review, quality policy and objectives, quality KPIs and cost of quality. |
| [`quality-manager-qms-iso13485`](skills/community/quality-manager-qms-iso13485/) | Build or maintain an ISO 13485 medical device QMS: design, documentation, CAPA, audit prep. |
| [`regulatory-affairs-head`](skills/community/regulatory-affairs-head/) | Plan medical device market access: FDA submissions, CE marking and agency responses. |
| [`risk-management-specialist`](skills/community/risk-management-specialist/) | ISO 14971 medical device risk management: hazard analysis, FMEA, fault trees, risk controls, benefit-risk or residual risk. |
| [`soc2-compliance`](skills/community/soc2-compliance/) | Prepare for SOC 2 audits: criteria mapping, control matrices, evidence and gap analysis. |

## Sources and licences

Third-party content keeps its own licence. Licence files are in the related folders. Skills were synced with the upstream commits below on 2026-11-07.

- Anthropic: Apache-2.0, https://github.com/anthropics/skills (`2c5958e`)
- Community: MIT, https://github.com/alirezarezvani/claude-skills (`8f08254`)
- Caveman: Apache-2.0 / MIT, https://github.com/JuliusBrussee/caveman (`c310c9d`)
- Firebase: Apache-2.0, https://github.com/firebase/agent-skills (`b76be96`)
- Scrapling: `skills/custom/scrapling-official/LICENSE.txt`, https://github.com/D4Vinci/Scrapling (`bc60248`)

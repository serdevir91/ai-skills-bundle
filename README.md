# AI Skills Bundle

A collection of 248 skills and example rules for Claude Code, Codex and similar AI agents. It contains no API keys, account IDs or private data.

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
| [`skills/community/`](#community-189) | 189 | Engineering, product, marketing, leadership and compliance roles |
| `rules/` | | Example `AGENTS.md` and `CLAUDE.md` rules |
| `scripts/` | | Hooks that shut down idle iOS Simulators |

`brand-guidelines` exists in both `anthropic` and `community`, so installing everything gives 247 unique skills.

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

### Community (189)

Role-based skills for engineering, product, marketing, leadership and compliance. Install with `./install.sh community`.

#### AI agents and LLM engineering (19)

| Skill | What it does |
|---|---|
| [`agent-designer`](skills/community/agent-designer/) | Design multi-agent systems, create agent architectures, define agent communication patterns, or build autonomous agent workflows. |
| [`agent-handoff`](skills/community/agent-handoff/) | Keep a central `agent.md` knowledge file to pass context between AI sessions. |
| [`agent-protocol`](skills/community/agent-protocol/) | Inter-agent communication protocol for C-suite agent teams. |
| [`agent-workflow-designer`](skills/community/agent-workflow-designer/) | Design multi-agent workflows with handoff contracts, failure handling and cost controls. |
| [`agenthub`](skills/community/agenthub/) | Multi-agent collaboration plugin that spawns N parallel subagents competing on the same task via git worktree isolation. |
| [`autoresearch-agent`](skills/community/autoresearch-agent/) | Autonomous experiment loop that optimizes any file by a measurable metric. |
| [`context-engine`](skills/community/context-engine/) | Loads and manages company context for all C-suite advisor skills. |
| [`llm-cost-optimizer`](skills/community/llm-cost-optimizer/) | Cut LLM API spend with model routing, prompt caching and cost observability. |
| [`mcp-server-builder`](skills/community/mcp-server-builder/) | Build MCP servers from API contracts. |
| [`prompt-engineer-toolkit`](skills/community/prompt-engineer-toolkit/) | Analyze and rewrite prompts and create reusable prompt templates. |
| [`prompt-governance`](skills/community/prompt-governance/) | Manage production prompts: versioning, A/B tests, registries and regression checks. |
| [`rag-architect`](skills/community/rag-architect/) | Design RAG pipelines, optimize retrieval strategies, choose embedding models, implement vector search, or build knowledge retrieval systems. |
| [`self-eval`](skills/community/self-eval/) | Honestly evaluate AI work quality using a two-axis scoring system. |
| [`self-improving-agent`](skills/community/self-improving-agent/) | Curate Claude Code's auto-memory into durable project knowledge. |
| [`senior-computer-vision`](skills/community/senior-computer-vision/) | Computer vision engineering skill for object detection, image segmentation, and visual AI systems. |
| [`senior-ml-engineer`](skills/community/senior-ml-engineer/) | ML engineering skill for productionizing models, building MLOps pipelines, and integrating LLMs. |
| [`senior-prompt-engineer`](skills/community/senior-prompt-engineer/) | Optimize prompts, design templates and evaluate LLM outputs. |
| [`skill-security-auditor`](skills/community/skill-security-auditor/) | Security audit and vulnerability scanner for AI agent skills before installation. |
| [`skill-tester`](skills/community/skill-tester/) | Validate, test and score skill quality. |

#### Software engineering (35)

| Skill | What it does |
|---|---|
| [`a11y-audit`](skills/community/a11y-audit/) | Scan, fix and verify WCAG 2.2 A/AA accessibility across major frontend frameworks. |
| [`adversarial-reviewer`](skills/community/adversarial-reviewer/) | Adversarial code review that breaks the self-review monoculture. |
| [`api-design-reviewer`](skills/community/api-design-reviewer/) | Review API designs against REST conventions and best practices. |
| [`api-test-suite-builder`](skills/community/api-test-suite-builder/) | Generate API tests, create integration test suites, test REST endpoints, or build contract tests. |
| [`browser-automation`](skills/community/browser-automation/) | Automate browser tasks, scrape websites, fill forms, capture screenshots, extract structured data from web pages, or build web automation workflows. |
| [`changelog-generator`](skills/community/changelog-generator/) | Generate release notes from Conventional Commits. |
| [`code-reviewer`](skills/community/code-reviewer/) | Automated code review for TypeScript, JavaScript, Python, Go, Swift and Kotlin. |
| [`code-to-prd`](skills/community/code-to-prd/) | Reverse-engineer any codebase into a complete Product Requirements Document (PRD). |
| [`codebase-onboarding`](skills/community/codebase-onboarding/) | Analyze a codebase and generate onboarding docs for new developers. |
| [`database-designer`](skills/community/database-designer/) | Design database schemas, plan data migrations, optimize queries, choose between SQL and NoSQL, or model data relationships. |
| [`database-schema-designer`](skills/community/database-schema-designer/) | Create ERD diagrams, normalize database schemas, design table relationships, or plan schema migrations. |
| [`dependency-auditor`](skills/community/dependency-auditor/) | Analyze and audit dependencies across multi-language projects. |
| [`focused-fix`](skills/community/focused-fix/) | Fix, debug, or make a specific feature/module/area work end-to-end. |
| [`git-worktree-manager`](skills/community/git-worktree-manager/) | Run parallel feature work with isolated Git worktrees, ports and environments. |
| [`migration-architect`](skills/community/migration-architect/) | Plan, execute and validate complex system migrations with minimal business impact. |
| [`monorepo-navigator`](skills/community/monorepo-navigator/) | Manage Turborepo, Nx, pnpm workspace and Lerna monorepos. |
| [`performance-profiler`](skills/community/performance-profiler/) | Profile Node.js, Python and Go apps for CPU, memory and I/O bottlenecks. |
| [`playwright-pro`](skills/community/playwright-pro/) | Production-grade Playwright testing toolkit. |
| [`pr-review-expert`](skills/community/pr-review-expert/) | Review pull requests, analyze code changes, check for security issues in PRs, or assess code quality of diffs. |
| [`release-manager`](skills/community/release-manager/) | Plan releases, manage changelogs, coordinate deployments, create release branches, or automate versioning. |
| [`saas-scaffolder`](skills/community/saas-scaffolder/) | Generate SaaS boilerplate with auth, database, billing and API routes. |
| [`senior-architect`](skills/community/senior-architect/) | Design system architecture and compare microservices with monoliths. |
| [`senior-backend`](skills/community/senior-backend/) | Designs and implements backend systems including REST APIs, microservices, database architectures, authentication flows, and security hardening. |
| [`senior-data-engineer`](skills/community/senior-data-engineer/) | Data engineering skill for building scalable data pipelines, ETL/ELT systems, and data infrastructure. |
| [`senior-data-scientist`](skills/community/senior-data-scientist/) | World-class senior data scientist skill specialising in statistical modeling, experiment design, causal inference, and predictive analytics. |
| [`senior-frontend`](skills/community/senior-frontend/) | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. |
| [`senior-fullstack`](skills/community/senior-fullstack/) | Scaffold Next.js, FastAPI, MERN and Django projects and analyze code quality. |
| [`senior-qa`](skills/community/senior-qa/) | Generates unit tests, integration tests, and E2E tests for React/Next.js applications. |
| [`snowflake-development`](skills/community/snowflake-development/) | Write Snowflake SQL, build pipelines and use Cortex AI functions. |
| [`spec-driven-workflow`](skills/community/spec-driven-workflow/) | Write specs and acceptance criteria before code, then generate tests from them. |
| [`sql-database-assistant`](skills/community/sql-database-assistant/) | Write and optimize SQL, generate migrations and work with ORMs. |
| [`stripe-integration-expert`](skills/community/stripe-integration-expert/) | Implement Stripe subscriptions, one-time payments, usage billing and checkout. |
| [`tdd-guide`](skills/community/tdd-guide/) | Guide test-driven development: unit tests, fixtures, mocks and coverage gaps. |
| [`tech-debt-tracker`](skills/community/tech-debt-tracker/) | Scan codebases for technical debt, score severity, track trends, and generate prioritized remediation plans. |
| [`tech-stack-evaluator`](skills/community/tech-stack-evaluator/) | Technology stack evaluation and comparison with TCO analysis, security assessment, and ecosystem health scoring. |

#### Cloud, DevOps and IT admin (15)

| Skill | What it does |
|---|---|
| [`aws-solution-architect`](skills/community/aws-solution-architect/) | Design AWS architectures for startups using serverless patterns and IaC templates. |
| [`azure-cloud-architect`](skills/community/azure-cloud-architect/) | Design Azure architectures for startups and enterprises. |
| [`ci-cd-pipeline-builder`](skills/community/ci-cd-pipeline-builder/) | Generate CI/CD pipelines from detected project stack signals. |
| [`docker-development`](skills/community/docker-development/) | Optimize Dockerfiles, compose setups, multi-stage builds and container security. |
| [`env-secrets-manager`](skills/community/env-secrets-manager/) | Audit environment variable hygiene, secrets safety and rotation readiness. |
| [`gcp-cloud-architect`](skills/community/gcp-cloud-architect/) | Design GCP architectures for startups and enterprises. |
| [`google-workspace-cli`](skills/community/google-workspace-cli/) | Google Workspace administration via the gws CLI. |
| [`helm-chart-builder`](skills/community/helm-chart-builder/) | Scaffold and review Helm charts, values and templates. |
| [`incident-commander`](skills/community/incident-commander/) | Manage technology incidents from detection through resolution. |
| [`ms365-tenant-manager`](skills/community/ms365-tenant-manager/) | Microsoft 365 tenant administration for Global Administrators. |
| [`observability-designer`](skills/community/observability-designer/) | Design observability strategies, including SLI/SLO/SLA frameworks. |
| [`runbook-generator`](skills/community/runbook-generator/) | Generate operational runbooks for deployment, incidents, maintenance and rollback. |
| [`secrets-vault-manager`](skills/community/secrets-vault-manager/) | Set up HashiCorp Vault and AWS, Azure or GCP secret stores. |
| [`senior-devops`](skills/community/senior-devops/) | Comprehensive DevOps skill for CI/CD, infrastructure automation, containerization, and cloud platforms (AWS, GCP, Azure). |
| [`terraform-patterns`](skills/community/terraform-patterns/) | Terraform module design, state management, provider configuration and security hardening. |

#### Security (8)

| Skill | What it does |
|---|---|
| [`ai-security`](skills/community/ai-security/) | Assess AI/ML systems for prompt injection, jailbreaks, data poisoning and tool abuse. |
| [`cloud-security`](skills/community/cloud-security/) | Assess cloud setups for misconfigurations, IAM escalation paths and public exposure. |
| [`incident-response`](skills/community/incident-response/) | Triage a security incident: classification, escalation and forensic evidence. |
| [`red-team`](skills/community/red-team/) | Plan authorized red team engagements and attack path analysis. |
| [`security-pen-testing`](skills/community/security-pen-testing/) | Run authorized security audits, vulnerability scans and OWASP Top 10 checks. |
| [`senior-secops`](skills/community/senior-secops/) | Senior SecOps engineer skill for application security, vulnerability management, compliance verification, and secure development practices. |
| [`senior-security`](skills/community/senior-security/) | Security engineering toolkit for threat modeling, vulnerability analysis, secure architecture, and penetration testing. |
| [`threat-detection`](skills/community/threat-detection/) | Hunt for threats, analyze IOCs and detect anomalies in telemetry. |

#### Product, design and project management (18)

| Skill | What it does |
|---|---|
| [`agile-product-owner`](skills/community/agile-product-owner/) | Agile product ownership for backlog management and sprint execution. |
| [`atlassian-admin`](skills/community/atlassian-admin/) | Administer Jira, Confluence, Bitbucket and Trello: users, permissions and security. |
| [`atlassian-templates`](skills/community/atlassian-templates/) | Create and manage Jira and Confluence templates, blueprints and layouts. |
| [`confluence-expert`](skills/community/confluence-expert/) | Atlassian Confluence expert for creating and managing spaces, knowledge bases, and documentation. |
| [`epic-design`](skills/community/epic-design/) | Build cinematic 2.5D websites with scroll storytelling and parallax depth. |
| [`experiment-designer`](skills/community/experiment-designer/) | Plan product experiments, testable hypotheses and sample sizes, and read A/B outcomes. |
| [`jira-expert`](skills/community/jira-expert/) | Manage Jira projects, JQL, workflows, custom fields, automation and reporting. |
| [`meeting-analyzer`](skills/community/meeting-analyzer/) | Analyzes meeting transcripts and recordings to surface behavioral patterns, communication anti-patterns, and actionable coaching feedback. |
| [`product-analytics`](skills/community/product-analytics/) | Define KPIs, dashboards, and cohort, retention and feature adoption analysis. |
| [`product-discovery`](skills/community/product-discovery/) | Validate opportunities, map assumptions and test problem-solution fit. |
| [`product-manager-toolkit`](skills/community/product-manager-toolkit/) | RICE prioritization, interview analysis, PRD templates and discovery frameworks. |
| [`product-strategist`](skills/community/product-strategist/) | OKR cascades, quarterly planning and competitive analysis for product leaders. |
| [`research-summarizer`](skills/community/research-summarizer/) | Structured research summarization agent skill for non-dev users. |
| [`roadmap-communicator`](skills/community/roadmap-communicator/) | Prepare roadmap narratives, release notes and stakeholder updates. |
| [`scrum-master`](skills/community/scrum-master/) | Advanced Scrum Master skill for data-driven agile team analysis and coaching. |
| [`senior-pm`](skills/community/senior-pm/) | Senior Project Manager for enterprise software, SaaS, and digital transformation projects. |
| [`ui-design-system`](skills/community/ui-design-system/) | Generate design tokens, component docs and responsive design calculations. |
| [`ux-researcher-designer`](skills/community/ux-researcher-designer/) | Create personas, journey maps and usability test plans. |

#### Marketing, SEO and growth (46)

| Skill | What it does |
|---|---|
| [`ab-test-setup`](skills/community/ab-test-setup/) | Plan, design, or implement an A/B test or experiment. |
| [`ad-creative`](skills/community/ad-creative/) | Generate, iterate, or scale ad creative for paid advertising. |
| [`ai-seo`](skills/community/ai-seo/) | Optimize content to get cited by AI search engines — ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Copilot. |
| [`analytics-tracking`](skills/community/analytics-tracking/) | Set up, audit, and debug analytics tracking implementation — GA4, Google Tag Manager, event taxonomy, conversion tracking, and data quality. |
| [`app-store-optimization`](skills/community/app-store-optimization/) | App Store Optimization: keyword research, competitor rankings and metadata suggestions. |
| [`brand-guidelines`](skills/community/brand-guidelines/) | Apply, document or enforce brand guidelines for any product or company. |
| [`campaign-analytics`](skills/community/campaign-analytics/) | Analyzes campaign performance with multi-touch attribution, funnel conversion analysis, and ROI calculation for marketing optimization. |
| [`churn-prevention`](skills/community/churn-prevention/) | Reduce voluntary and involuntary churn through cancel flow design, save offers, exit surveys, and dunning sequences. |
| [`cold-email`](skills/community/cold-email/) | Write, improve, or build a sequence of B2B cold outreach emails to prospects who haven't asked to hear from them. |
| [`competitive-teardown`](skills/community/competitive-teardown/) | Analyze competitors from pricing pages, reviews, job posts, SEO and social signals. |
| [`competitor-alternatives`](skills/community/competitor-alternatives/) | Create competitor comparison or alternative pages for SEO and sales enablement. |
| [`content-creator`](skills/community/content-creator/) | Deprecated redirect that routes old content requests to the right specialist skill. |
| [`content-humanizer`](skills/community/content-humanizer/) | Makes AI-generated content sound genuinely human — not just cleaned up, but alive. |
| [`content-production`](skills/community/content-production/) | Full content production pipeline — takes a topic from blank page to published-ready piece. |
| [`content-strategy`](skills/community/content-strategy/) | Plan a content strategy, decide what content to create, or figure out what topics to cover. |
| [`copy-editing`](skills/community/copy-editing/) | Edit, review, or improve existing marketing copy. |
| [`copywriting`](skills/community/copywriting/) | Write or improve marketing copy for any page. |
| [`email-sequence`](skills/community/email-sequence/) | Create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. |
| [`email-template-builder`](skills/community/email-template-builder/) | Build transactional email systems with React Email templates and provider integration. |
| [`form-cro`](skills/community/form-cro/) | Optimize lead capture, contact, demo and survey forms for conversion. |
| [`free-tool-strategy`](skills/community/free-tool-strategy/) | Build a free tool for marketing — lead generation, SEO value, or brand awareness. |
| [`landing-page-generator`](skills/community/landing-page-generator/) | Generates high-converting landing pages as complete Next.js/React (TSX) components with Tailwind CSS. |
| [`launch-strategy`](skills/community/launch-strategy/) | Plan a product launch, feature announcement, or release strategy. |
| [`marketing-context`](skills/community/marketing-context/) | Create and maintain the marketing context document that all marketing skills read before starting. |
| [`marketing-demand-acquisition`](skills/community/marketing-demand-acquisition/) | Plan demand generation, paid spend, SEO and partnership campaigns. |
| [`marketing-ideas`](skills/community/marketing-ideas/) | Generate marketing ideas and strategies for SaaS products. |
| [`marketing-ops`](skills/community/marketing-ops/) | Central router for the marketing skill ecosystem. |
| [`marketing-psychology`](skills/community/marketing-psychology/) | Apply psychological principles, mental models, or behavioral science to marketing. |
| [`marketing-strategy-pmm`](skills/community/marketing-strategy-pmm/) | Product marketing skill for positioning, GTM strategy, competitive intelligence, and product launches. |
| [`onboarding-cro`](skills/community/onboarding-cro/) | Optimize post-signup onboarding, user activation, first-run experience, or time-to-value. |
| [`page-cro`](skills/community/page-cro/) | Optimize, improve, or increase conversions on any marketing page — including homepage, landing pages, pricing pages, feature pages, or blog posts. |
| [`paid-ads`](skills/community/paid-ads/) | Plan and optimize campaigns on Google, Meta, LinkedIn and X. |
| [`paywall-upgrade-cro`](skills/community/paywall-upgrade-cro/) | Create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. |
| [`popup-cro`](skills/community/popup-cro/) | Create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. |
| [`pricing-strategy`](skills/community/pricing-strategy/) | Design, optimize, and communicate SaaS pricing — tier structure, value metrics, pricing pages, and price increase strategy. |
| [`programmatic-seo`](skills/community/programmatic-seo/) | Create SEO-driven pages at scale using templates and data. |
| [`referral-program`](skills/community/referral-program/) | Design, launch, or optimize a referral or affiliate program. |
| [`schema-markup`](skills/community/schema-markup/) | Implement, audit and validate structured data on a website. |
| [`seo-audit`](skills/community/seo-audit/) | Audit and diagnose SEO issues on a site. |
| [`signup-flow-cro`](skills/community/signup-flow-cro/) | Optimize signup, registration, account creation, or trial activation flows. |
| [`site-architecture`](skills/community/site-architecture/) | Plan website structure, URL hierarchy, navigation and internal linking. |
| [`social-content`](skills/community/social-content/) | Create and schedule content for LinkedIn, X, Instagram, TikTok and Facebook. |
| [`social-media-analyzer`](skills/community/social-media-analyzer/) | Social media campaign analysis and performance tracking. |
| [`social-media-manager`](skills/community/social-media-manager/) | Plan social strategy, content calendars and community engagement. |
| [`video-content-strategist`](skills/community/video-content-strategist/) | Plan video strategy, scripts, YouTube growth and short-form pipelines. |
| [`x-twitter-growth`](skills/community/x-twitter-growth/) | X/Twitter growth engine for building audience, crafting viral content, and analyzing engagement. |

#### Leadership, business and operations (35)

| Skill | What it does |
|---|---|
| [`board-deck-builder`](skills/community/board-deck-builder/) | Assembles comprehensive board and investor update decks by pulling perspectives from all C-suite roles. |
| [`board-meeting`](skills/community/board-meeting/) | Multi-agent board meeting protocol for strategic decisions. |
| [`business-investment-advisor`](skills/community/business-investment-advisor/) | Business investment analysis and capital allocation advisor. |
| [`ceo-advisor`](skills/community/ceo-advisor/) | Executive leadership guidance for strategic decision-making, organizational development, and stakeholder management. |
| [`cfo-advisor`](skills/community/cfo-advisor/) | Financial leadership for startups and scaling companies. |
| [`change-management`](skills/community/change-management/) | Framework for rolling out organizational changes without chaos. |
| [`chief-of-staff`](skills/community/chief-of-staff/) | Orchestrate and route work across the C-suite advisor skills. |
| [`chro-advisor`](skills/community/chro-advisor/) | People leadership for scaling companies. |
| [`ciso-advisor`](skills/community/ciso-advisor/) | Security leadership for growth-stage companies. |
| [`cmo-advisor`](skills/community/cmo-advisor/) | Marketing leadership for scaling companies. |
| [`company-os`](skills/community/company-os/) | The meta-framework for how a company runs — the connective tissue between all C-suite roles. |
| [`competitive-intel`](skills/community/competitive-intel/) | Systematic competitor tracking that feeds CMO positioning, CRO battlecards, and CPO roadmap decisions. |
| [`contract-and-proposal-writer`](skills/community/contract-and-proposal-writer/) | Draft contracts, proposals, SOWs, NDAs and MSAs for several jurisdictions. |
| [`coo-advisor`](skills/community/coo-advisor/) | Operations leadership for scaling companies. |
| [`cpo-advisor`](skills/community/cpo-advisor/) | Product leadership for scaling companies. |
| [`cro-advisor`](skills/community/cro-advisor/) | Revenue leadership for B2B SaaS companies. |
| [`cs-onboard`](skills/community/cs-onboard/) | Founder onboarding interview that captures company context across 7 dimensions. |
| [`cto-advisor`](skills/community/cto-advisor/) | Technical leadership guidance for engineering teams, architecture decisions, and technology strategy. |
| [`culture-architect`](skills/community/culture-architect/) | Build, measure, and evolve company culture as operational behavior — not wall posters. |
| [`customer-success-manager`](skills/community/customer-success-manager/) | Monitors customer health, predicts churn risk, and identifies expansion opportunities using weighted scoring models for SaaS customer success. |
| [`decision-logger`](skills/community/decision-logger/) | Two-layer memory architecture for board meeting decisions. |
| [`executive-mentor`](skills/community/executive-mentor/) | Adversarial thinking partner for founders and executives. |
| [`financial-analyst`](skills/community/financial-analyst/) | Performs financial ratio analysis, DCF valuation, budget variance analysis, and rolling forecast construction for strategic decision-making. |
| [`founder-coach`](skills/community/founder-coach/) | Personal leadership development for founders and first-time CEOs. |
| [`internal-narrative`](skills/community/internal-narrative/) | Build and maintain one coherent company story across all audiences — employees, investors, customers, candidates, and partners. |
| [`interview-system-designer`](skills/community/interview-system-designer/) | Design hiring pipelines, interview loops and calibration. |
| [`intl-expansion`](skills/community/intl-expansion/) | International market expansion strategy. |
| [`ma-playbook`](skills/community/ma-playbook/) | M&A strategy for acquiring companies or being acquired. |
| [`org-health-diagnostic`](skills/community/org-health-diagnostic/) | Cross-functional organizational health check combining signals from all C-suite roles. |
| [`revenue-operations`](skills/community/revenue-operations/) | Analyzes sales pipeline health, revenue forecasting accuracy, and go-to-market efficiency metrics for SaaS revenue optimization. |
| [`saas-metrics-coach`](skills/community/saas-metrics-coach/) | SaaS financial health advisor. |
| [`sales-engineer`](skills/community/sales-engineer/) | Analyze RFP gaps, build feature comparison matrices and plan POCs. |
| [`scenario-war-room`](skills/community/scenario-war-room/) | Cross-functional what-if modeling for cascading multi-variable scenarios. |
| [`strategic-alignment`](skills/community/strategic-alignment/) | Cascades strategy from boardroom to individual contributor. |
| [`team-communications`](skills/community/team-communications/) | Write 3P updates, newsletters, FAQ roundups and incident reports. |

#### Compliance and quality (13)

| Skill | What it does |
|---|---|
| [`capa-officer`](skills/community/capa-officer/) | CAPA system management for medical device QMS. |
| [`fda-consultant-specialist`](skills/community/fda-consultant-specialist/) | FDA regulatory consultant for medical device companies. |
| [`gdpr-dsgvo-expert`](skills/community/gdpr-dsgvo-expert/) | GDPR and German DSGVO compliance automation. |
| [`information-security-manager-iso27001`](skills/community/information-security-manager-iso27001/) | ISO 27001 ISMS implementation and cybersecurity governance for HealthTech and MedTech companies. |
| [`isms-audit-expert`](skills/community/isms-audit-expert/) | Audit an ISO 27001 ISMS: controls, compliance checks and certification prep. |
| [`mdr-745-specialist`](skills/community/mdr-745-specialist/) | EU MDR 2017/745 compliance specialist for medical device classification, technical documentation, clinical evidence, and post-market surveillance. |
| [`qms-audit-expert`](skills/community/qms-audit-expert/) | ISO 13485 internal audit expertise for medical device QMS. |
| [`quality-documentation-manager`](skills/community/quality-documentation-manager/) | Document control system management for medical device QMS. |
| [`quality-manager-qmr`](skills/community/quality-manager-qmr/) | Senior Quality Manager Responsible Person (QMR) for HealthTech and MedTech companies. |
| [`quality-manager-qms-iso13485`](skills/community/quality-manager-qms-iso13485/) | ISO 13485 Quality Management System implementation and maintenance for medical device organizations. |
| [`regulatory-affairs-head`](skills/community/regulatory-affairs-head/) | Senior Regulatory Affairs Manager for HealthTech and MedTech companies. |
| [`risk-management-specialist`](skills/community/risk-management-specialist/) | Medical device risk management specialist implementing ISO 14971 throughout product lifecycle. |
| [`soc2-compliance`](skills/community/soc2-compliance/) | Prepare for SOC 2 audits: criteria mapping, control matrices, evidence and gap analysis. |

## Sources and licences

Third-party content keeps its own licence. Licence files are in the related folders.

- Anthropic: Apache-2.0, https://github.com/anthropics/skills
- Community: MIT, https://github.com/alirezarezvani/claude-skills
- Caveman: Apache-2.0 / MIT, https://github.com/JuliusBrussee/caveman
- Firebase: Apache-2.0, https://github.com/firebase/agent-skills
- Scrapling: `skills/custom/scrapling-official/LICENSE.txt`, https://github.com/D4Vinci/Scrapling

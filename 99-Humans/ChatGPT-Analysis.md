---
microservice: obsidian-brain
type: documentation
status: active
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#type/documentation'
- '#state/active'
- role/human-onboarding
---
# ChatGPT Analysis

Date: 2026-05-20

## Short Diagnosis

This folder is not a simple notes directory. It is an Obsidian-based command center for the Bastien-Antigravity ecosystem. Its purpose is to act as the shared memory, governance layer, documentation system, and AI orchestration hub for a multi-repository software fleet.

The repository combines:

- human-readable Obsidian documentation;
- AI operating instructions and session state;
- Behavior-Driven Development specifications;
- technical architecture and coding standards;
- microservice hub documentation;
- fleet-wide repo inventory and deployment logs;
- local automation scripts;
- a local RAG/MCP semantic search engine.

In practical terms, `obsidian-brain` is the place where the system decides what should be built, how it should be built, which rules agents must follow, and how the broader fleet should stay synchronized.

## Main Purpose

The vault serves four primary functions.

1. **Strategic memory**

   The AI agents are treated as stateless workers. They do not rely on conversational memory alone. Instead, the vault stores project DNA, session state, strategic audits, architecture decisions, behavior specs, and operational logs so a new AI session can reconstruct context quickly.

2. **AI governance**

   Files such as `00-AI-Orchestration/AI-Init.md`, `00-AI-Orchestration/AI-Project-DNA.md`, and `00-AI-Orchestration/MODE-MANUAL.md` define how AI agents should initialize, what constraints they must respect, and which workflow mode is active.

3. **Fleet command**

   `05-Fleet-Operation` contains the multi-repository inventory, fleet action plans, deployment logs, GitHub/CI standards, and automation around synchronization. It treats the broader Bastien-Antigravity ecosystem as one coordinated fleet rather than a set of isolated repositories.

4. **Knowledge retrieval**

   `08-RAG-Engine` implements a local MCP server and vector index so AI tools can query the vault semantically instead of reading large numbers of Markdown files directly. This is designed to reduce token usage and keep AI work grounded in the current vault.

## How The Folder Is Organized

The structure follows a numbered knowledge architecture.

| Folder | Role |
| --- | --- |
| `00-AI-Orchestration` | Global AI rules, project DNA, session state, mode manual, templates |
| `01-Strategic-Nexus` | Strategic audits, long-term patterns, anti-backlog, Oracle-style analysis |
| `02-Business-BDD` | Behavior specs, glossary, acceptance criteria, Frozen safety zone |
| `03-Tech-Stack` | Architecture rules, coding standards, deployment standards |
| `04-Rapid-Prototyping` | Experimental work and fast-path labs |
| `05-Fleet-Operation` | Fleet inventory, action plans, deployment logs, CI/CD standards |
| `06-Microservices` | Operational hub pages for each service |
| `07-Core-KMS` | Agent prompts, workflows, tag taxonomy, knowledge-management rules |
| `08-RAG-Engine` | Local semantic search and MCP bridge for AI agents |
| `20-Scripts` | Automation scripts for squad startup, mode switching, audits, scaffolding |
| `99-Humans` | Human-facing dashboards, explanations, and onboarding material |

There are also Obsidian configuration files under `.obsidian`, AI-agent integration folders such as `.gemini` and `.deepseek`, virtual environments, and Git metadata.

## Operating Model

The vault is built around a few core concepts.

### 1. Modes

The active mode is stored in `00-AI-Orchestration/MODE-MANUAL.md`. At the time of this analysis, the active mode is:

```yaml
active_mode: 4
```

Mode 4 is **Direct-Action**, intended for tactical work, small repairs, one-off audits, and direct interaction without heavy state overhead.

The documented modes are:

- **Mode 1: Spec-First**: high-safety workflow where BDD specs are mandatory.
- **Mode 2: Free-Labs**: fast experimental workflow.
- **Mode 3: Fleet-Commander**: multi-repo synchronization and refactor workflow.
- **Mode 4: Direct-Action**: lightweight tactical workflow.

### 2. Zones

The vault separates work by safety and scope.

- **Zone 1: Frozen**: `02-Business-BDD`, the behavioral source of truth.
- **Zone 2: Fluid**: `04-Rapid-Prototyping`, the experimentation area.
- **Zone 3: Fleet**: `05-Fleet-Operation`, the operational command layer.

This separation is meant to prevent experimental work from contaminating validated specifications or fleet-level operations.

### 3. MOCs And Links

The main navigation point is `Ecosystem-Map-MOC.md`. It links to the major areas of the vault and acts as the root map of content.

The system uses Obsidian-style bidirectional links, YAML frontmatter, tags, and dashboards. Markdown files are treated almost like structured records: frontmatter is metadata, tags are classification fields, and links define relationships.

### 4. Session State

`AI-Session-State.md` and `00-AI-Orchestration/AI-Session-State.md` are used as hard-state memory between sessions. The documented workflow expects agents to read session state at startup and update it before closing important work.

### 5. AI Squad

The vault defines specialized roles such as Orchestrator, Architect, Developer, QA, Sentinel, FleetArchitect, FleetCommander, DocMaintainer, Purger, and Strategic Oracle. Their prompts and workflows live mainly under `07-Core-KMS`.

The intended interaction model is delegation: the human asks the appropriate agent role to perform a task, and that role uses the vault rules and relevant context.

## Automation And Runtime Behavior

The most important automation entry points are:

- `20-Scripts/start_squad.py`
- `20-Scripts/switch_mode.py`
- `20-Scripts/vault-sentinel.py`
- `05-Fleet-Operation/00-Repo-Control/fleet-manager.py`
- `08-RAG-Engine/main.py`

### `start_squad.py`

This is the main launcher for the AI squad environment. It:

- detects and re-executes inside the local Python virtual environment when available;
- runs preflight/governance checks when matching scripts exist;
- synchronizes role prompts into agent definitions;
- lets the operator select an active mode;
- configures MCP servers for Gemini and Claude;
- prefers the local RAG engine when available;
- falls back to a filesystem MCP server if the RAG engine is unavailable;
- launches the selected CLI engine, with fallback behavior across supported engines.

### `switch_mode.py`

This script changes the operating protocol by updating:

- `00-AI-Orchestration/MODE-MANUAL.md`;
- `00-AI-Orchestration/AI-Session-State.md`;
- root `AI-Session-State.md`.

It keeps the mode manual and session-state protocol aligned.

### `vault-sentinel.py`

This script audits Markdown files for tag taxonomy and Obsidian link coherence. It uses `20-Scripts/lib/sovereignty.py` and the taxonomy source in `07-Core-KMS/tag_taxonomy.md`.

It can also repair malformed frontmatter tags when run with `--fix`.

### `08-RAG-Engine`

The RAG engine provides a local MCP server over stdio. It indexes the workspace into ChromaDB using local embeddings and exposes tools such as:

- `query_brain`;
- `get_brain_stats`;
- `find_similar_files`;
- workspace file read/write helpers guarded by access rules.

The RAG layer includes:

- Markdown parsing;
- YAML frontmatter flattening;
- paragraph/window chunking;
- ChromaDB vector storage;
- a file watcher;
- mode-aware exclusions;
- an access matrix.

Its purpose is to give AI agents a token-efficient way to retrieve relevant vault knowledge.

## Fleet Function

`05-Fleet-Operation/00-Repo-Control/inventory.json` lists the broader repository fleet. The inventory includes the internal brain modules and many external service repositories such as:

- `config-server`;
- `data-ingestor`;
- `distributed-config`;
- `docker-deployment`;
- `enhanced-backtesting`;
- `fundamental-analysis`;
- `log-server`;
- `market-observer`;
- `notif-server`;
- `orderbook-aggregator`;
- `safe-socket`;
- `sandbox-testing`;
- `technical-analysis`;
- `tele-remote`;
- `web-interface`.

Most repositories are configured around the `develop` branch. The fleet layer exists to coordinate standards, synchronization, CI/CD, deployments, and cross-repo refactors.

## Human-Facing Layer

`99-Humans` is the human-readable area. It contains:

- dashboards;
- architecture summaries;
- testing guidance;
- domain overviews;
- simplified explanations of how to operate the brain.

This layer is intentionally separate from the core AI orchestration material so humans can inspect and control the system without reading every operational prompt or automation file.

## Current Folder State Observed

The folder currently contains mostly Markdown and Python outside of virtual environments:

- about 305 Markdown files;
- about 45 Python files;
- YAML/JSON configuration;
- Obsidian canvas/config files;
- local virtual environments and generated Python cache files.

The Git working tree had pre-existing uncommitted changes at the time of this analysis:

- modified `.obsidian/workspace.json`;
- modified `20-Scripts/convert_agents.py`;
- untracked `.deepseek/`;
- untracked `20-Scripts/clients/API/deepseek_client.py`.

Those items were not modified by this analysis.

## Strengths

- The vault has a clear strategic purpose: preserving context and governance for AI-assisted development.
- The numbered folder layout is predictable.
- The `Ecosystem-Map-MOC.md` gives a strong central navigation point.
- The mode system gives the operator a way to trade off safety, speed, and scope.
- The RAG engine is a practical answer to context-window limits.
- The fleet inventory makes cross-repo operations explicit instead of informal.
- The human-facing `99-Humans` layer helps make the system auditable by a person.

## Risks And Friction Points

- The system is complex. A new operator needs to understand Obsidian, AI roles, modes, zones, fleet management, and RAG before using it confidently.
- There is potential duplication between root-level state files and files under `00-AI-Orchestration`.
- The runtime behavior depends on local tools and environments: Python venvs, Gemini or other CLIs, MCP configuration, Node/npm, and local embeddings.
- Some scripts write outside the vault into user-level AI configuration directories such as Gemini and Claude settings. This is powerful but should be treated carefully.
- The RAG engine and access matrix add a second control layer. If docs, mode state, and RAG permissions drift, agents may behave inconsistently.
- Generated/cache folders and local environment artifacts can make repository scans noisy unless consistently excluded.

## Practical Way To Use This Folder

For a human operator:

1. Start with `README.md`, `User-Manual.md`, and `Ecosystem-Map-MOC.md`.
2. Check the active mode in `00-AI-Orchestration/MODE-MANUAL.md`.
3. Read `AI-Session-State.md` before continuing previous work.
4. Use `99-Humans` for simplified dashboards and explanations.
5. Use `20-Scripts/start_squad.py` when launching the intended AI squad workflow.
6. Use `02-Business-BDD` before changing stable product behavior.
7. Use `04-Rapid-Prototyping` for experiments.
8. Use `05-Fleet-Operation` for multi-repo work.
9. Use `08-RAG-Engine` when AI context retrieval needs to be semantic and token-efficient.

## Bottom Line

`obsidian-brain` is the central operating memory for the Bastien-Antigravity ecosystem. It is designed to make AI-assisted software development less ad hoc by giving agents a persistent knowledge base, explicit roles, enforceable workflows, semantic retrieval, and fleet-level operational control.

Its real function is not just documentation. It is an AI-readable and human-auditable control plane for building, testing, coordinating, and governing a large multi-service software system.

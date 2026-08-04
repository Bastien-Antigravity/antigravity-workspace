---
microservice: obsidian-brain
type: documentation
status: active
tags:
- '#service/obsidian-brain'
- '#type/documentation'
- '#state/active'
- '#zone/3-fleet'
---
# Bastien-Antigravity: Ecosystem Map 🔗

![[README]]

## 🛰️ 05 - Fleet Operations
Fleet-wide action plans, deployment logs, and migration states. **(Zone 3: Fleet)**
- [[05-Fleet-Operation/README|Fleet Operations (Zone 3)]]
- **Command Center**: [[05-Fleet-Operation/00-Repo-Control/inventory.json|Global Repo Registry]]
- **Automation**: `fleet-manager.py` (Mass Sync & Audit)
- **Logs**: [[05-Fleet-Operation/Deployment-Logs-MOC|🛰️ Deployment Logs Index]]
- **Strategy**: [[05-Fleet-Operation/05-Fleet-Strategy/04-CICD-Standards|CI/CD Standards]]
- [[05-Fleet-Operation/05-Fleet-Strategy/01-GitHub-Standard|🐙 GitHub Standards]]
- [[05-Fleet-Operation/05-Fleet-Strategy/03-CD-Lifecycle|🔄 CD Lifecycle Management]]

## 🌐 06 - Microservices
Live documentation and operational hubs for the service fleet.
- **[[06-Microservices/Hubs-MOC|🌐 Cross-Repo Hubs Index]]**
- **[[06-Microservices/Config-Server-Hub|🌐 Config-Server Hub]]** (Go)
- **[[06-Microservices/Log-Server-Hub|🌐 Log-Server Hub]]** (Rust)
- **[[06-Microservices/Notif-Server-Hub|🌐 Notif-Server Hub]]** (Go)
- **[[06-Microservices/Safe-Socket-Hub|🌐 Safe-Socket Hub]]** (Go/SHM)
- **[[06-Microservices/Distributed-Config-Hub|🌐 Distributed-Config Hub]]** (Go/Polyglot)
- **[[06-Microservices/Market-Observer-Hub|🌐 Market-Observer Hub]]** (Go)
- **[[06-Microservices/Data-Ingestor-Hub|🌐 Data-Ingestor Hub]]** (Go)
- **[[06-Microservices/Orderbook-Aggregator-Hub|🌐 Orderbook-Aggregator Hub]]** (Go)
- **[[06-Microservices/Fundamental-Analysis-Hub|🌐 Fundamental-Analysis Hub]]** (Python)
- **[[06-Microservices/Technical-Analysis-Hub|🌐 Technical-Analysis Hub]]** (Python)
- **[[06-Microservices/Web-Interface-Hub|🌐 Web-Interface Hub]]** (Go)
- **[[06-Microservices/Enhanced-Backtesting-Hub|🌐 Enhanced-Backtesting Hub]]** (Rust)
- **[[06-Microservices/Docker-Deployment-Hub|🐳 Docker-Deployment Hub]]**
- **[[06-Microservices/Sandbox-Testing-Hub|🧪 Sandbox-Testing Hub]]**
- **[[06-Microservices/Tele-Remote-Hub|🛰️ Tele-Remote Hub]]**
- [[06-Microservices/Universal-Logger-Hub|Universal-Logger Hub]]
- **[[06-Microservices/Ontime-Scheduler-Hub|🌐 Ontime-Scheduler Hub]]** (Rust)

### 📜 Technical Protocols
- [[06-Microservices/Microservice-Startup-Protocol|📜 Microservice Startup & CLI Protocol]]
- [[06-Microservices/Microservice-Logging-Standard|📜 Microservice Logging Standard]]
- [[06-Microservices/Unified-Control-Protocol|📜 Unified Control Protocol (gRPC/REST)]]
- [[06-Microservices/Web-Interface-Integration-Protocol|📜 Web Interface Integration Protocol]]

## 🧠 07 - Core KMS
Knowledge Management System, Agent Role Prompts, and Workflows.
- [[07-Core-KMS/README|KMS Overview]]
- [[07-Core-KMS/tag_taxonomy|🏷️ Tag Taxonomy (Source of Truth)]]
- [[07-Core-KMS/Agent-Roles-MOC|🤖 Agent Roles Index]]
- [[07-Core-KMS/00-Knowledge-Management-Playbook|📐 Knowledge Management Playbook]]
- [[00-AI-Orchestration/Workflows/Daily-AI-Playbook|📖 Daily AI Playbook]]
- **👥 Agent Squad (Role Prompts & Wisdom)**:
  - [[07-Core-KMS/Role-Prompts/01-Orchestrator/Prompt-Orchestrator|🎭 Role 01: Orchestrator]]
  - [[07-Core-KMS/Role-Prompts/02-Architect/Prompt-Architect|📐 Role 02: Architect]]
  - [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|💻 Role 03: Lead Developer]]
  - [[07-Core-KMS/Role-Prompts/04-QA/Prompt-QA|🧪 Role 04: QA]]
  - [[07-Core-KMS/Role-Prompts/05-FleetArchitect/Prompt-Fleet-Architect|🏛️ Role 05: Fleet Architect]]
  - [[07-Core-KMS/Role-Prompts/06-DocMaintainer/Prompt-DocMaintainer|📚 Role 06: DocMaintainer]]
  - [[07-Core-KMS/Role-Prompts/07-FleetCommander/Prompt-FleetCommander|🛰️ Role 07: Fleet Commander]]
  - [[07-Core-KMS/Role-Prompts/08-Purger/Mister-Straight-to-Goal|🧹 Role 08: Purger]]
  - [[07-Core-KMS/Role-Prompts/09-Sentinel/Prompt-Sentinel|🛡️ Role 09: Sentinel]]

## 🧠 09 - RAG Engine
Local sovereign semantic search and real-time knowledge watcher.
- [[09-RAG-Engine/README|RAG Engine Overview]]
- [[09-RAG-Engine/README|🔌 Setup & Usage Guide]]
- **Available Agent Tools**:
  - `query_brain(query: str, zone_filter: str = None, limit: int = 3)` — Sub-paragraph level semantic vector query.
  - `get_brain_stats()` — Fetch active database volume and indexing status.
  - `find_similar_files(filepath: str)` — Semantic similarity relationship lookup.

## 🤖 10 - Agent Factory
Object-oriented framework for orchestrating squads of autonomous LLM-driven agents.
- [[10-Agent-Factory/README|Agent Factory Overview]]
- **Methodology & Guides**:
  - [[10-Agent-Factory/docs/00_Agent_Engineering_MOC|🗺️ Agent Engineering & Evaluation MOC]]
  - [[10-Agent-Factory/docs/ingenierie_agents|1. Spécifications & Arbitrage Code vs LLM]]
  - [[10-Agent-Factory/docs/implementation_pratique|2. Implémentation Pratique (Boilerplate)]]
  - [[10-Agent-Factory/docs/lexique_et_syntaxe|3. Lexique, Syntaxe et Robustesse Lexicale]]
  - [[10-Agent-Factory/docs/evaluation_rag_et_connaissances|4. Évaluation du RAG et des Connaissances]]
  - [[10-Agent-Factory/docs/securite_et_gardes_fous|5. Sécurité, Garde-fous et Injections]]
  - [[10-Agent-Factory/docs/coordination_et_multi_agents|6. Coordination & Systèmes Multi-Agents]]
  - [[10-Agent-Factory/docs/observabilite_et_reporting|7. Observabilité, Traces et Dérives]]
  - [[10-Agent-Factory/docs/gestion_des_couts_et_cache|8. Coûts, Cache & Rate-Limiting]]
  - [[10-Agent-Factory/docs/workflow_et_automatisation|9. Workflow de Développement (TDD) & Makefile]]

## ⚡ Dashboards & Foundry
Live sprint tracking and standardized templates.
- [[99-Humans/Sprint-Dashboard|⚡ Live Sprint Dashboard]]
- [[99-Humans/Domain-Dashboard|🌐 Domain Ontology Matrix]]
- [[00-AI-Orchestration/Templates/Template-00-Idea-Pitch|📥 Task Inbox (Foundry)]]

## 🛠️ 08 - Base Scripts
Ecosystem automation scripts.
- [[08-Base-Scripts/main.py|main.py]] — Unified CLI Entrypoint Router.
  - Run **Purger**: `python3 08-Base-Scripts/main.py joint-audit-purger`
  - Run **Squad Launcher**: `python3 08-Base-Scripts/main.py start-squad`
  - Run **Vault Sentinel**: `python3 08-Base-Scripts/main.py brain-health-audit`

---
## 🧪 Quality & Testing
Quality Assurance follows a two-layer architecture:
1. **Definition Layer** (`02-Business-BDD`): Behavior specs written in markdown BDD format (Given/When/Then).
2. **Execution Layer** (`sandbox-testing`): Automated test scenarios that validate the behavior specs against real infrastructure.

The flow is: `02-Business-BDD` (WHAT) → `sandbox-testing` (HOW) → microservice (CODE).
---

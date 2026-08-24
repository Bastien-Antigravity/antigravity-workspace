---
microservice: obsidian-brain
type: documentation
status: active
tags:
- '#service/obsidian-brain'
- '#type/documentation'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# Bastien-Antigravity: Obsidian Brain 🌌

Welcome to the **Obsidian Brain**. This repository is the central Strategic Command Center and Knowledge Management System (KMS) for the Bastien-Antigravity ecosystem.

It is designed as a **Multi-Mode Engine** to balance between rigorous infrastructure hardening and rapid experimentation.

---

## 🕹️ Command & Control
This Brain is an **Operational Engine**. Use the following scripts to govern the AI Squad:
- **`python3 08-Base-Scripts/start_squad.py`**: Launches the AI client with an interactive **Mode Selector** (defaults to the `gemini` CLI).
- **`pip install -r requirements.txt`**: Installs vault-level launcher/client dependencies. `start_squad.py` checks and installs missing packages automatically.
- **`python3 08-Base-Scripts/switch_mode.py`**: Quick-switch between **Spec-First**, **Labs**, and **Fleet** protocols.
- **Configuring the Active Client**:
  * **Via Frontmatter**: Define `active_client: antigravity` (or `gemini`/`claude`/`codex`/`deepseek`) inside ****'s YAML header.
  * **Via Environment Variable**: Override or boot directly using:
    ```bash
    ACTIVE_CLIENT=antigravity python3 08-Base-Scripts/start_squad.py
    ```
  * **Compatibility**: `ACTIVE_CLI` still works as an alias for older commands.
  * **Fallback System**: If your chosen CLI is not available, the squad launcher automatically sweeps through fallbacks (`antigravity`, `gemini`, `claude`, `codex`, `deepseek`) to launch the first available engine. DeepSeek is API-backed through `08-Base-Scripts/clients/API/deepseek_client.py` and requires `DEEPSEEK_API_KEY`.
  * **DeepSeek API Setup**: Prefer shell environment variables:
    ```bash
    export DEEPSEEK_API_KEY="sk-..."
    export DEEPSEEK_BASE_URL="https://api.deepseek.com"
    export DEEPSEEK_MODEL="deepseek-chat"
    ```
    `DEEPSEEK_BASE_URL` and `DEEPSEEK_MODEL` are optional. See [AI-Client-Startup-Guide.md](99-Humans/AI-Client-Startup-Guide.md).

---

## ⚡ Quick Start: RAG Database Hydration (PostgreSQL + pgvector)

When cloning this project from GitHub, spin up the local `pgvector` database and hydrate RAG data in seconds:

```bash
# 1. Start PostgreSQL with pgvector container (runs on port 5432)
docker-compose -f docker-compose.db.yml up -d

# 2. Setup RAG Engine python virtualenv
cd 09-RAG-Engine
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Hydrate local database from repository seed package
python3 main.py import-seed --in data/seed

# 4. Export updated seed dataset (when modifying docs or code)
python3 main.py export-seed --out data/seed
```

---

## 👤 Human Onboarding
Before interacting with the AI Squad, human operators should read the structural guides:
- **** — Start here to understand the 4-Tier & 3-Zone system.
- **** — How to start Gemini, Claude, Codex, or DeepSeek.
- **** — Purpose, concepts, mental models, and optimization tips.
- **** — How we ensure quality across Knowledge, Behavior, and Code.
- **** — High-level onboarding and usage guide.
- **** — The central navigation hub for the vault.
- **** — Detailed protocol rules.

---

## 🏗️ The 3-Zone Architecture
To prevent "Mode Leakage," the vault is organized into three distinct operational zones:

1.  **🛡️ Zone 1: Frozen (02-Business-BDD)**: Behavioral Source of Truth. Contains approved BDD specs (Gherkin). No code changes allowed without a matching spec here.
2.  **🧪 Zone 2: Fluid (04-Rapid-Prototyping)**: Experimental Labs. Fast-path development, UI mockups, and "Labs" sprints.
3.  **🛰️ Zone 3: Fleet (05-Fleet-Operation)**: Global Operations. Tracks fleet-wide action plans, deployment logs, and migration states.

---

## 🛠️ How it Works (5D Paradigm)
The documentation here relies on a hybrid system:
1. **Shallow Folders (PARA/Diátaxis):** We separate generic workflows (`07-Core-KMS`) from specific rules (`03-Tech-Stack`).
2. **Strategic MOCs:** Navigation is driven by **Maps of Content**. Start every session at the ****.
3. **Live Dashboards:** Uses Obsidian Dataview to dynamically track Tasks and Bugs across the fleet.
4. **Visual Topologies:** Infinite 2D boards (Obsidian Canvas) for infrastructure mapping.
5. **Bidirectional Links:** A Zettelkasten-style graph of architectural decisions.

---

## 🧑‍💻 Human Mode (Developer Guide)
1. **Install Obsidian:** Download the app.
2. **Configure:** Follow ****.
3. **Start at the MOC:** Open ****. This is your entry point.
4. **Authoring:** Keep files atomic. Use `Links` to connect concepts.

---

## 🎮 The 3 Levels of AI Engagement

This Brain is designed to be used in three distinct ways, depending on your needs for safety, speed, or specialization.

### 1. 🛡️ Mode-Based Execution (Global Protocols)
Best for enforcing repo-wide "Rules of Engagement." 
- **Usage**: Update the `active_mode` in ****.
- **Impact**: Sets the global protocol (e.g., **Spec-First** requires BDD specs before code).

### 2. 🧠 The AI Squad (Custom Subagent Prompts)
Best for delegating isolated, specialized tasks to an expert persona.
- **Usage**: Use the configured AI client delegation system (via `08-Base-Scripts/start_squad.py`).
- **Examples**: *"Ask QA to review the tests"* or *"Ask the Architect to check the blueprint."*
- **Impact**: Uses dedicated subagent definitions in `.gemini/agents/`, `.claude/agents/`, `.codex/agents/`, or `.deepseek/agents/` with built-in drift mitigation (SCAN).

### 3. 💬 Direct AI Interaction (Raw Orchestrator)
Best for general brainstorming, repo exploration, or "Free-Form" work.
- **Usage**: Talk directly to the main Gemini CLI without specific mode or subagent delegation.

---

## 🤖 Assistant Initialization (MANDATORY)
Regardless of how you interact with the AI, every session MUST be initialized correctly to maintain context reliability across your repositories.

1. **Start the Engine**: Run `./08-Base-Scripts/start_squad.py` from the vault root.
2. **Restore State**: At the start of every session, you MUST instruct the AI to read the **** file and restore the ****. 
3. **Save State**: Before closing a session, ensure the AI has updated the **** with a summary of progress. This acts as our "Hard State" context block.

---

## 🧠 The Semantic Search Engine (RAG-mcp)
To guarantee optimal token efficiency during AI squad sessions, the repository features an integrated Model Context Protocol (MCP) server: ****.
* **Offline Embeddings**: Uses a local vector database index via PostgreSQL (pgvector) and `BAAI/bge-m3` embeddings to perform sub-paragraph level queries.
* **Auto-Watcher**: Silently starts a background thread-safe file watcher directly inside the FastMCP server process with a `0.5s` quiet-window debounce to capture note updates instantly without SQLite lock contentions.
* **Custom Tools**: Exposes `query_brain`, `get_brain_stats`, and semantic graph lookups via `find_similar_files`.

---

> [!CAUTION]
> Never implement code without verifying the current **Active Protocol** in the .

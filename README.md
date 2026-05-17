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
# Bastien-Antigravity: Obsidian Brain 🌌

Welcome to the **Obsidian Brain**. This repository is the central Strategic Command Center and Knowledge Management System (KMS) for the Bastien-Antigravity ecosystem.

It is designed as a **Multi-Mode Engine** to balance between rigorous infrastructure hardening and rapid experimentation.

---

## 🕹️ Command & Control
This Brain is an **Operational Engine**. Use the following scripts to govern the AI Squad:
- **`python3 20-Scripts/start_squad.py`**: Launches the CLI with an interactive **Mode Selector**.
- **`python3 20-Scripts/switch_mode.py`**: Quick-switch between **Spec-First**, **Labs**, and **Fleet** protocols.

---

## 👤 Human Onboarding
Before interacting with the AI Squad, human operators should read the structural guides:
- **[[99-Humans/Architecture-Overview|🗺️ Global Architecture Overview]]** — Start here to understand the 4-Tier & 3-Zone system.
- **[[99-Humans/General-Misc|🧠 Philosophy & Operator's Guide]]** — Purpose, concepts, mental models, and optimization tips.
- **[[99-Humans/Testing-Playbook|🧪 Testing Playbook]]** — How we ensure quality across Knowledge, Behavior, and Code.
- **[[User-Manual|📖 User Manual]]** — High-level onboarding and usage guide.
- **[[Ecosystem-Map-MOC|🔗 Ecosystem Map (MOC)]]** — The central navigation hub for the vault.
- **[[00-AI-Orchestration/MODE-MANUAL|🕹️ Mode Manual]]** — Detailed protocol rules.

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
2. **Strategic MOCs:** Navigation is driven by **Maps of Content**. Start every session at the **[[Ecosystem-Map-MOC]]**.
3. **Live Dashboards:** Uses Obsidian Dataview to dynamically track Tasks and Bugs across the fleet.
4. **Visual Topologies:** Infinite 2D boards (Obsidian Canvas) for infrastructure mapping.
5. **Bidirectional Links:** A Zettelkasten-style graph of architectural decisions.

---

## 🧑‍💻 Human Mode (Developer Guide)
1. **Install Obsidian:** Download the app.
2. **Configure:** Follow **[[03-Tech-Stack/03-Project-Coding/Documentation-Requirements|Documentation Standards]]**.
3. **Start at the MOC:** Open **[[Ecosystem-Map-MOC]]**. This is your entry point.
4. **Authoring:** Keep files atomic. Use `Links` to connect concepts.

---

---
## 🎮 The 3 Levels of AI Engagement

This Brain is designed to be used in three distinct ways, depending on your needs for safety, speed, or specialization.

### 1. 🛡️ Mode-Based Execution (Global Protocols)
Best for enforcing repo-wide "Rules of Engagement." 
- **Usage**: Update the `active_mode` in **[[00-AI-Orchestration/MODE-MANUAL]]**.
- **Impact**: Sets the global protocol (e.g., **Spec-First** requires BDD specs before code).

### 2. 🧠 The AI Squad (Custom Subagent Prompts)
Best for delegating isolated, specialized tasks to an expert persona.
- **Usage**: Use the Gemini CLI delegation system (via `20-Scripts/start_squad.py`).
- **Examples**: *"Ask QA to review the tests"* or *"Ask the Architect to check the blueprint."*
- **Impact**: Uses a dedicated subagent definition in `.gemini/agents/` with built-in drift mitigation (SCAN).

### 3. 💬 Direct AI Interaction (Raw Orchestrator)
Best for general brainstorming, repo exploration, or "Free-Form" work.
- **Usage**: Talk directly to the main Gemini CLI without specific mode or subagent delegation.

---

## 🤖 Assistant Initialization (MANDATORY)
Regardless of how you interact with the AI, every session MUST be initialized correctly to maintain context reliability across your repositories.

1. **Start the Engine**: Run `./20-Scripts/start_squad.py` from the vault root.
2. **Restore State**: At the start of every session, you MUST instruct the AI to read the **[[00-AI-Orchestration/AI-Init]]** file and restore the **[[00-AI-Orchestration/AI-Session-State]]**. 
3. **Save State**: Before closing a session, ensure the AI has updated the **[[00-AI-Orchestration/AI-Session-State]]** with a summary of progress. This acts as our "Hard State" context block.

> [!CAUTION]
> Never implement code without verifying the current **Active Protocol** in the [[00-AI-Orchestration/MODE-MANUAL]].

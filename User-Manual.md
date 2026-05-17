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
# 🌌 Bastien-Antigravity: Obsidian Brain User Manual

Welcome to the **Obsidian Brain**. This is the Strategic Command Center for the Bastien-Antigravity ecosystem. It bridges high-level strategy with autonomous AI execution through a specialized Multi-Agent Squad.

---

## 🛠️ 1. Prerequisites (Ground Zero)

Before you begin, ensure your environment is configured:

1. **Python 3.10+**: Required for the automation scripts. To avoid polluting your system's global Python packages, you **must** use the provided virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Node.js**: Required to run the MCP Filesystem servers.
3. **Gemini CLI**: Install via npm:
   ```bash
   npm install -g @google/gemini-cli
   ```
4. **Auth**: Run `gemini /auth signin` to link your Google account or Google AI Pro account.
5. IDE: **Antigravity IDE** or **Vscode** and **gemini-cli** extension is recommanded but not mandatory...

---

## 🚀 2. Launch Sequence (From 0 to Run)

Follow these steps to activate the ecosystem:

### Step 1: Initialize the Squad

This script configures the MCP "Filesystem Bridge" and prepares the subagents.

```bash
    # Ensure your virtual environment is active first!
    source .venv/bin/activate
    python3 obsidian-brain/20-Scripts/start_squad.py
```

### Step 2: Connect the IDE (Optional but Recommended)

If the CLI asks "Do you want to connect Antigravity?", select **1. Yes**. This allows the terminal to sync with your VS Code/Cursor editor.

### Step 3: Verify the Tools

Inside the Gemini CLI, verify the vault is bound:

> `/mcp list`
> *(You should see `obsidian_vault` with tools like `read_file` and `list_directory`)*

### Step 4: Warm Up the Session

Always start by restoring the context from the hard-state files:

> *"@AI-Init.md @AI-Session-State.md [SCAN] Initialize session."*

---

## 🤖 3. How to Talk to the Squad (Examples)

The system is built for **delegation**. Instead of asking a single AI, ask a specialist:

### Scenario A: The Integrity Audit (QA Specialist)

Audit your documentation gaps:

> *"Ask **QA** to use the `obsidian_vault` tool to compare the microservices in `06-Microservices` against the specs in `02-Business-BDD`. List any missing specs in a table."*

### Scenario B: Architectural Design (Architect)

Design a new system component:

> *"Ask **Architect** to read the `Log-Server-Hub` and propose an ADR for a new 'Batch-Upload' feature. Save the result as a draft in `03-Tech-Stack/ADRs/`."*

### Scenario C: Feature Implementation (Developer)

Write code based on a spec:

> *"Ask **Developer** to implement the logic defined in `@02-Business-BDD/Notif-Server-Retries.feature`. Focus on the Rust implementation in the `notif-server` repository."*

---

## 📐 4. The 2-Digit Structure

To keep navigation predictable for both humans and AI, the vault follows this numbering:

| Folder                             | Purpose                  | Governance               |
| ---------------------------------- | ------------------------ | ------------------------ |
| **`00-AI-Orchestration`**  | Meta-Logic & Templates   | Global Rules & Foundry   |
| **`01-Strategic-Nexus`**   | Strategic Oracle Brain   | Analysis Only            |
| **`02-Business-BDD`**      | **Zone 1: Frozen** | Behavior Specs (Gherkin) |
| **`03-Tech-Stack`**        | Architecture & Standards | ADRs & Wisdom            |
| **`04-Rapid-Prototyping`** | **Zone 2: Fluid**  | Experimental Labs        |
| **`05-Fleet-Operation`**   | **Zone 3: Fleet**  | Multi-Repo Inventory     |
| **`06-Microservices`**     | Service Hubs             | Operational Docs         |
| **`07-Core-KMS`**          | AI Agent Engine          | Agent Prompts (OS)       |
| **`20-Scripts`**           | Automation               | CLI Scripts              |

---

## 🛡️ 5. Managing Operational Modes

The Brain has three distinct "Protocols" that change how the AI works. You can switch between them at startup or anytime during your session.

### How to Switch:

1. **At Startup**: The `start_squad.py` script now asks you to select a mode before the CLI begins.
2. **Anytime**: Run the standalone switcher script:
   ```bash
   python3 20-Scripts/switch_mode.py
   ```
3. **The "Oracle" Command**: You can also ask the AI to do it: *"Switch to Mode 2 and update the manual."*

### The 3 Modes:

- **Mode 1: Spec-First**: No code without a BDD spec. High safety.
- **Mode 2: Free-Labs**: Experimental speed. BDD is optional.
- **Mode 3: Fleet-Commander**: Scale mode for multi-repo refactors.

---

---

## 🤖 6. The AI Squad Dossier

Each agent has a specialized persona and access level. Use the `/agents list` command in the CLI to see who is available.

| Agent | Purpose | Primary Tools |
|-------|---------|---------------|
| **Orchestrator** | High-level mission planning and task delegation. | `obsidian_vault`, `shell` |
| **Architect** | Designs system blueprints, ADRs, and gRPC schemas. | `obsidian_vault` |
| **Developer** | Writes polyglot code (Go, Rust, Python, C++). | `shell`, `read_file`, `write_file` |
| **QA** | Audits code against BDD specs and sandbox standards. | `obsidian_vault`, `shell` |
| **Sentinel** | Integrity auditor. Monitors persona drift and protocol adherence. | `obsidian_vault` |
| **Strategic Oracle**| Strategic analysis. Identifies long-term patterns and blind spots. | `obsidian_vault` (Strategic Oracle) |
| **FleetArchitect**| Manages cross-repository dependencies and global CI/CD. | `obsidian_vault` (Fleet Operation) |
| **FleetCommander**| Handles global Git sync, releases, and deployment logs. | `shell`, `obsidian_vault` |
| **DocMaintainer** | Keeps the Obsidian vault clean, repairs links, and logs sessions. | `obsidian_vault` |
| **Purger** | Cleanup specialist. Removes redundant code and documentation drift. | `shell`, `obsidian_vault` |

---

## 🔄 7. Mode Behavior Matrix

The agents change their behavior based on the `active_mode` set in `MODE-MANUAL.md`.

| Role | 🛡️ Mode 1: Spec-First | 🧪 Mode 2: Free-Labs | 🛰️ Mode 3: Fleet |
|------|-----------------------|----------------------|------------------|
| **Developer** | **BLOCKED** until BDD spec is approved. | **UNLEASHED**. Rapid MVP iteration. | Focus on global refactors. |
| **QA / Sentinel** | **STRICT**. Rejects any drift from specs. | **PASSIVE**. Monitoring only. | **CRITICAL**. Audits fleet stability. |
| **Architect** | Formal ADRs required for every change. | Rapid sketches and prototypes. | Global topology mapping. |
| **Orchestrator** | Sequential, slow, safe steps. | Multi-tasking, fast delegation. | Strategic mission coordination. |

---

## 🛡️ 8. The "Golden Rules" of Engagement

1. **The SCAN Protocol**: Every agent response MUST start with `[SCAN]` to verify Role, Source, and State.
2. **Hard-Stop Context**: Never end a session without asking the AI to: *"Update AI-Session-State.md with today's progress."*
3. **MOC First**: If you get lost, go to **[[Ecosystem-Map-MOC]]**. It is the single source of truth for all links.

---

## 🧪 9. The Validation Loop: Trust through Testing

The entire Bastien-Antigravity ecosystem relies on a **"Trust, but Verify"** model. We do not assume the AI's code is correct because it "looks" right; we assume it is correct only when it **passes the tests.**

### The Trinity of Truth:
- **The Spec (WHAT)**: Defined in `02-Business-BDD`. This is the behavioral contract.
- **The Code (HOW)**: Written by the **Developer** in the microservice repositories.
- **The Test (PROOF)**: Executed in the `sandbox-testing` environment. 

### Why this matters:
1. **Verification over Explanation**: An agent might explain its code beautifully but still fail an edge case. The **QA Agent** is programmed to prioritize the test output over the Developer's explanation.
2. **Regression Safety**: By keeping BDD specs in the "Frozen Zone," we ensure that a new update in `rapid-prototyping` doesn't break a core system logic.
3. **Automated Audits**: The **Sentinel** can run the full test suite across the fleet to ensure that global refactors didn't cause "Silent Failures" in distant repositories.

> [!TIP]
> Always ask the **QA Agent**: *"Run the automated tests for this feature and show me the raw output."* This is the ultimate defense against AI drift.

---

## 🎨 10. Visualizing the Brain: The Obsidian App

While the AI Squad operates in the terminal, you can (and should) keep the **Obsidian App** open on your second monitor. This serves as your **Visual Control Panel**.

### Why use the Obsidian App?
1. **Real-Time Auditing**: As the AI Squad writes a new BDD spec or updates a Session Log, you will see the changes appear in the Obsidian app instantly. This is the fastest way to verify the AI's "Reasoning" visually.
2. **The Graph View**: Open the Graph View to see how your `02-Business-BDD` specs are linked to your `06-Microservices`. If you see a cluster without any links, you've found a documentation gap!
3. **Live Dashboards**: Use the **[[Ecosystem-Map-MOC]]** as your home screen. It uses **Dataview** queries to automatically list every repository, its language, and its current status.

> [!IMPORTANT]
> The Obsidian Brain is designed to be **Human-Readable**. If an AI agent creates a folder or file that looks messy or disorganized in the Obsidian app, it has failed the structural standard. Correct it immediately!

---

## 🏗️ 11. Scaling Up: Fabricating a New Brain

If you want to start a **completely new project** (e.g., a Marketing campaign, a new SaaS, or a Research paper) while keeping this exact AI architecture, you can "Fabricate" a new brain in seconds.

### The Scaffolding Command:
From the root of your current brain, run:
```bash
python3 20-Scripts/scaffold_new_brain.py
```

### What happens?
1. **Architecture Clone**: All 10 numbered zones (`00-20`) are created in a new folder.
2. **Intelligence Transfer**: Your entire AI Squad (Role Prompts) and Automation Scripts (start_squad, switch_mode) are copied over.
3. **Business Wipe**: The `02-Business-BDD` and `06-Microservices` folders are left **EMPTY**, ready for your new project's unique logic.
4. **Auto-Bake**: The script automatically runs the agent conversion so the new CLI is ready to use immediately.

### Why use this?
This allows you to treat your **AI Infrastructure** as a reusable asset. You build the "Squad" once, and then you deploy it to any new "World" (project) you want to build.

---

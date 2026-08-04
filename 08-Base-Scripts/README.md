---
microservice: obsidian-brain
type: automation
status: active
tags:
- '#service/obsidian-brain'
- '#type/automation'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🕹️ Bastien-Antigravity: Base Scripts

This directory contains the core operational scripts for the Bastien-Antigravity AI Squad and Knowledge Management System (KMS). It acts as the "Engine Room" for the entire ecosystem.

---

## 🚀 Quick Start

### 1. Installation
The scripts depend on the virtual environment located in the vault root.
```bash
# From the obsidian-brain root
pip install -r requirements.txt
```

### 2. Launch the AI Squad
The primary entry point is the unified CLI router `main.py`. It initializes the environment, synchronizes personas, and launches your preferred AI client.
```bash
python3 08-Base-Scripts/main.py start-squad
```

---

## 🛠️ Core Toolset

All tools are unified under the `main.py` router:

| Command | Purpose |
| :--- | :--- |
| `python3 08-Base-Scripts/main.py start-squad` | **Main Orchestrator**. Handles pre-session audits, role sync, and launches the AI client. |
| `python3 08-Base-Scripts/main.py fleet-commander` | **Fleet Manager**. Performs mass Git operations and architecture audits. |
| `python3 08-Base-Scripts/main.py switch-mode` | **Protocol Switcher**. Atomically toggles between Spec-First, Labs, and Fleet modes. |
| `python3 08-Base-Scripts/main.py check-coherence` | **Integrity Auditor**. Ensures runtime agent skills are 100% coherent with vault prompts. |
| `python3 08-Base-Scripts/main.py persona-extractor`| **RAG Engine Helper**. Scans the codebase to extract patterns for AI context. |
| `python3 08-Base-Scripts/main.py knowledge-compressor` | **Memory Manager**. Distills session logs into actionable patterns. |
| `python3 08-Base-Scripts/main.py scaffold-new-brain` | **Generator**. Creates new repositories or vault sections following standards. |

---

## 📁 Directory Structure

- **`src/commands/`**: Implementation of CLI command modules.
- **`src/clients/`**: Implementation of AI client wrappers (Antigravity, Gemini, Codex).
- **`src/lib/`**: Shared library logic, including the `Sovereignty` engine for architectural audits.

---

## 🛡️ Governance & Safety
Most scripts include a **Bootstrap** phase that resolves the vault root and ensures the correct Python environment and library paths are loaded.

- **Preflight Checks**: `main.py start-squad` runs a mandatory audit before every session.
- **Mode Guardrails**: Enforcement of `MODE-MANUAL.md` rules is handled by `switch-mode`.
- **Hard-Stop State**: Every session-ending script updates `AI-Session-State.md` to prevent context loss.

---

## 🤝 Contributing
See [[CONTRIBUTING]] for guidelines on adding new scripts or clients to the engine room.

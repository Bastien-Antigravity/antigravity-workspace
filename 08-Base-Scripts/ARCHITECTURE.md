---
microservice: obsidian-brain
type: automation
status: active
tags:
- '#service/obsidian-brain'
- '#type/automation'
- '#state/active'
- '#zone/3-fleet'
---# 🏗️ Architecture: Base Scripts

The `08-Base-Scripts` directory follows a **Command-and-Control (C2)** architecture pattern designed for high-autonomy AI orchestration.

---

## 🧩 Component Map

### 1. The Orchestration Layer
- **`start_squad.py`**: The central nervous system. It doesn't just launch a client; it orchestrates a **Lifecycle**:
    1. **Audit**: Checks for unauthorized changes (via `sovereignty.py`).
    2. **Sync**: Rebuilds runtime `.agents/` from vault source (via `convert_agents.py`).
    3. **Protocol**: Locks the session into a specific Mode (via `switch_mode.py`).
    4. **Launch**: Hands off control to the selected Client.

### 2. The Fleet Layer
- **`fleet-commander.py`**: Operates at the workspace level. It uses `inventory.json` from `05-Fleet-Operation` to map and manage the 29 sub-repositories.
- **`lib/sovereignty.py`**: The "Customs Officer" of the fleet. It verifies that every repository adheres to the `.github` exclusion rules and standard file structures.

### 3. The Knowledge Layer
- **`persona_extractor.py`**: Uses AST (Python) and RegEx (Go/Rust) to build a semantic map of the codebase.
- **`knowledge-compressor.py`**: Implements a "Context Decay" mitigation strategy by distilling logs into patterns.

---

## 📡 Data Flow: AI Client Initialization

1.  **User** runs `start_squad.py`.
2.  **Orchestrator** loads `clients/registry.py` to find available engines.
3.  **Orchestrator** calls `convert_agents.py` to ensure the AI's "brain" matches the latest vault documentation.
4.  **Orchestrator** invokes `switch_mode.py` to prompt the user for an operational protocol.
5.  **Subprocess** launches the CLI (e.g., `gemini-cli`) with the correct agent and workspace context.

---

## 🛠️ Shared Libraries (`lib/`)

- **`sovereignty.py`**:
    - `ArchitectureAudit`: Validates repo archetypes (Microservice vs. Polyglot).
    - `Compliance`: Enforces CI/CD exclusion rules.
- **`orchestration_lib.py`** (referenced):
    - Terminal setup, path resolution, and vault/workspace discovery.

---

## 🤖 Client Registry (`clients/`)

The system is client-agnostic. Adding a new AI engine requires:
1.  Adding a entry in `clients/registry.py`.
2.  Implementing a wrapper in `clients/API/` (if it's an API-based client).
3.  Ensuring the `agents_dir` mapping is correct for persona synchronization.

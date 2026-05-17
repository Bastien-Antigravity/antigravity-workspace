---
microservice: obsidian-brain
type: documentation
status: active
tags:
- \'#zone/3-fleet\'
- \'#service/obsidian-brain\'
- '#type/documentation'
- '#state/active'
- role/human-onboarding
---

# 🧪 Testing Playbook: The Quality Engine

This document explains the multi-layered testing strategy of the Bastien-Antigravity ecosystem. We don't just test code; we test **Knowledge, Behavior, and Fleet Integrity.**

---

## 🏗️ 1. The 3-Layer Testing Architecture

Our testing is split into three distinct "Realities":

1.  **🧠 Semantic Testing (The Brain)**: Ensuring the Knowledge Management System (KMS) is coherent.
2.  **🎭 Behavioral Testing (The Sandbox)**: Ensuring the system does what we promised (Given/When/Then).
3.  **🛰️ Fleet Testing (The Reality)**: Ensuring all 25+ repositories are synchronized and standard-compliant.

---

## 🧠 2. Semantic & Structural Testing (Brain Health)

We treat our documentation as a "Graph Database." If a link is broken, the AI loses context. We use **Maintainer Scripts** to prevent this.

### 🛡️ The Sentinel (Brain-Health-Audit.py)
This is the primary "Sovereignty Audit" for the Obsidian Brain. It runs every time you start the squad.
- **What it checks**: YAML compliance, internal `[[Link]]` integrity, and "Orphaned" files.
- **Execution**: `python3 07-Core-KMS/Scripts/Brain-Health-Audit.py`
- **Goal**: 100% Coherence. If the Sentinel detects "Drift," you must resolve it before proceeding.

### 🔗 Link Verification
For quick, targeted link audits across the vault:
- **Execution**: `python3 verify_links_script.py`

---

## 🎭 3. Behavioral Testing (BDD & Sandbox)

We use **Behavior-Driven Development (BDD)** to bridge the gap between human requirements and AI execution.

### ❄️ Zone 1: Frozen Specs
All requirements start in **02-Business-BDD**. These are the "What". They define scenarios using:
- **Given**: The initial state.
- **When**: The action taken.
- **Then**: The expected outcome.

### 🧪 The Sandbox Testing Hub
Technical implementations (the "How") live in the `sandbox-testing` repository.
- **Scenario Orchestrator**: A specialized tool (`scenario_orchestrator.py`) that links the BDD specs to actual Go/Rust/Python test logic.
- **Dual Mode**: Tests can run in **Native** mode (local machine) or **Docker** mode (isolated infrastructure).

---

## 🛰️ 4. Fleet & Infrastructure Testing

Testing the "Connective Tissue" between repositories.

### 🚢 Fleet Manager (fleet-manager.py)
Manages the health of the entire ecosystem.
- **Audit Mode**: `python3 fleet-manager.py audit`. This checks every repo for CI/CD status (GitHub Actions), Dependabot health, and standard metadata.
- **Sync Validation**: Ensures all repos are on the correct branch (`develop`) and have no "Dark Matter" (untracked files).

### 🛫 Preflight Checks
Before any AI session begins, the `start_squad.py` script runs a "Preflight" to verify that:
- The `obsidian_vault` MCP server is correctly bound.
- The environment variables are set.
- The AI agents are "Freshly Regenerated" (via `convert_agents.py`).

---

## 👤 5. The Human Testing Experience

As a human operator, your testing role focuses on **Validation & Graduation**.

1.  **Graduation Ceremony**: When a prototype in **Zone 2 (Fluid)** works, you "test" it by forcing it to graduate. This means writing the BDD specs and moving it to **Zone 1 (Frozen)**.
2.  **Manual Verification**: Use the **Ecosystem-Map-MOC** and **Live Dashboards** to visually verify that the AI is reporting the correct status of the fleet.
3.  **Semantic Link Testing**: In Obsidian, use the **Graph View** to see if your new feature is properly connected to the existing knowledge. If it's an "Island," it's not fully tested.

---
> [!IMPORTANT]
> If the **Sentinel** report shows Errors, do NOT implement new features. Clean the Brain first. Reliability comes from Structural Coherence.

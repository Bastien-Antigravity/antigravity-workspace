---
microservice: ecosystem-core
type: architecture
status: active
tags:
- '#service/ecosystem-core'
- '#type/architecture'
- '#state/active'
- '#zone/0-orchestration'
---
# 📐 Level 00: AI Orchestration (Base Layer & Context Gatekeeper)

This document defines the role, structure, and principles of **Level 00 (00-AI-Orchestration)**, which serves as the foundation of the nested capability architecture.

---

## 🏛️ 1. Concept: The Nested Filesystem Merge Pattern

The `obsidian-brain` vault is built on a **conceptually nested capability stack** structured from `00` to `...`. 

*   **Filesystem Merge**: While the folders (`00-AI-Orchestration`, `01-Strategic-Nexus`, etc.) are checked out as independent Git repositories (submodules), they merge into a single local workspace directory layout.
*   **Upstream Dependence**: Higher levels depend on lower levels. Level 00 is the **absolute base layer**. It has zero upstream dependencies and must be self-contained so that the ecosystem can boot even if all other submodules are missing.
*   **Context Isolation**: By separating concerns into double-digit directories, we restrict the AI's active search space. An agent only loads the context folders relevant to its target capability level, saving tokens and preventing reasoning drift.

---

## 🎯 2. Purpose of Level 00

Level 00 anchors the **active state, configuration variables, and intake gatekeeping** of the ecosystem. It exists to:
1.  **Enforce Session Memory**: Maintain the active session log and task list so that consecutive chats do not suffer from amnesia.
2.  **Govern Active Modes**: Set the rules for tool execution and validation gates (Mode 1 to 4).
3.  **Gate Incoming Requests**: Standardize user intent into structured packages before downstream agent roles (such as Developer or QA) write any code.

---

## 📂 3. Directory Layout & Components

All files within this level reside inside the `00-AI-Orchestration/` folder:

```
00-AI-Orchestration/
├── MODE-MANUAL.md          # Governance mode selection (Modes 1 to 4)
├── AI-Session-State.md     # Active session checklist and task log (state anchor)
├── AI-Project-DNA.md       # High-level vision and system-wide constraints
├── Project-Variables.md    # Registry of local repo paths and workspace configurations
├── workflows/              # Declarative YAML templates for engine execution pipelines
│   ├── doc-sync.yaml
│   └── feature-implementation.yaml
└── Templates/              # Markdown templates to bootstrap session tasks
    ├── Template-00-AI-Task.md
    └── Template-00-Fast-Track.md
```

---

## 🎭 4. Agent Persona: The Context Gatekeeper

*   **Prompt Path**: `07-Core-KMS/Role-Prompts/01-Orchestrator/Prompt-Orchestrator.md` (or compiled under `.gemini/agents/orchestrator.md`).
*   **Objective**: Intake raw requests, run the **"Grill-Me" clarification loop** to verify targets and test boundaries, and compile the final `[INTAKE PACKAGE]` to delegate to the squad.

---
*References: [[Ecosystem-Map-MOC]], [[07-Knowledge-Management-Playbook]]*

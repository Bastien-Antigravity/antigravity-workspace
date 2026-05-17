---
microservice: obsidian-brain
type: documentation
status: active
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#type/architecture'
- '#state/active'
- role/human-onboarding
---
# 🌌 Bastien-Antigravity: Architecture Overview

Welcome, Human. This document provides a high-level visual and structural map of the **Bastien-Antigravity Ecosystem**. It explains how the Knowledge Management System (KMS), the AI Squad, and the Microservice Fleet work together.

---

## 🏗️ The 4-Tier AI-KMS Architecture

The ecosystem is built on a layered knowledge hierarchy. This separation ensures that the **Stateless AI Engine** can be updated globally without conflicting with project-specific logic.

```mermaid
graph TD
    subgraph "Tier 1: Core Logic"
        T1["🧠 07-Core-KMS<br/>(Stateless AI Prompts & Workflows)"]
    end

    subgraph "Tier 2: The Rulebook"
        T2["🏗️ 03-Tech-Stack<br/>(Coding, Architecture & CI/CD Rules)"]
    end

    subgraph "Tier 3: The Behavior"
        T3["🧪 02-Business-BDD<br/>(What the system should do - Gherkin)"]
    end

    subgraph "Tier 4: The Execution"
        T4["🚀 Fleet / Microservices<br/>(Actual Code & Implementation)"]
    end

    T1 --> T2
    T2 --> T3
    T3 --> T4
```

- **Tier 1 (Core)**: The "Operating System." Pure instructions for the AI agents.
- **Tier 2 (Stack)**: The "Engineering Standards." Defines how we build (Go, Rust, Python).
- **Tier 3 (Behavior)**: The "Product Specs." Human-readable Given/When/Then requirements.
- **Tier 4 (Fleet)**: The "Reality." The actual microservices running in the real world.

---

## 🛡️ The 3-Zone Operational Strategy

To balance **Speed** vs **Safety**, the `obsidian-brain` vault is divided into three operational zones.

```mermaid
flowchart LR
    subgraph Zone2 ["🧪 Zone 2: FLUID"]
        Fluid["04-Rapid-Prototyping<br/>(Experiments & Labs)"]
    end

    subgraph Zone1 ["🛡️ Zone 1: FROZEN"]
        Frozen["02-Business-BDD<br/>(Behavioral Source of Truth)"]
    end

    subgraph Zone3 ["🛰️ Zone 3: FLEET"]
        Fleet["05-Fleet-Operation<br/>(Global Ops & Deployment)"]
    end

    Fluid -- "Graduation Ceremony" --> Frozen
    Frozen -- "Implementation Sync" --> Fleet
```

1.  **Zone 1: Frozen (Spec-First)**: High-safety zone. No code changes allowed without matching BDD specs.
2.  **Zone 2: Fluid (Labs)**: High-speed zone. Rapid experimentation and "Idea-to-Code" sprints.
3.  **Zone 3: Fleet (Operations)**: The command center for the 25+ repositories. Tracks logs, migrations, and fleet health.

---

## 🎮 Command & Control (Orchestration)

The ecosystem is orchestrated by the **AI Squad**, managed through centralized scripts in the vault root.

| Tool | Purpose | Key File |
| :--- | :--- | :--- |
| **Squad Orchestrator** | Launches the AI CLI with Protocol Modes. | `20-Scripts/start_squad.py` |
| **Fleet Commander** | Manages mass-repo commits, syncs, and branches. | `05-Fleet-Operation/00-Repo-Control/fleet-manager.py` |
| **Strategic Oracle** | Analyzes logs to prevent architectural drift. | `01-Strategic-Nexus/` |
| **DocMaintainer** | Enforces metadata standards and link health. | `07-Core-KMS/Role-Prompts/05-DocMaintainer/` |

---

## 🔗 Repository Structure (The Submodule Hub)

`obsidian-brain` acts as the **Parent Wrapper**. All other "Brains" are injected as Git Submodules to ensure atomic updates and portability.

```mermaid
graph LR
    Root["📁 obsidian-brain (Wrapper)"]
    Root --> S1["📁 01-Strategic-Nexus"]
    Root --> S2["📁 02-Business-BDD"]
    Root --> S3["📁 03-Tech-Stack"]
    Root --> S4["📁 04-Rapid-Prototyping"]
    Root --> S5["📁 05-Fleet-Operation"]
    Root --> S7["📁 07-Core-KMS"]
    Root --> S6["📁 06-Microservices (Hubs)"]
    
    style Root fill:#1a1b26,stroke:#7aa2f7,stroke-width:2px,color:#fff
```

---

## ⚡ The Life of a Feature

1.  **Ideation**: A "Pitch" is written in `04-Rapid-Prototyping`.
2.  **Prototyping**: The AI builds a working demo in a Lab branch.
3.  **Refinement**: The feature "Graduates." BDD specs are moved to `02-Business-BDD`.
4.  **Implementation**: The Lead Developer implements the code in the target Microservice.
5.  **Verification**: The QA Agent verifies the code against the BDD specs using `sandbox-testing`.
6.  **Deployment**: The Fleet Commander pushes the verified changes to the global fleet.

---

## 🛰️ The Transversal Intelligence Layer

Beyond the standard build-pipeline, the ecosystem is governed by **Transversal Roles**. These agents operate across all tiers to ensure long-term stability and strategic coherence.

```mermaid
graph LR
    subgraph "Transversal Governance"
        OR["👁️ Chronos-Oracle<br/>(Strategic Memory)"]
        DM["🧹 DocMaintainer<br/>(Knowledge Health)"]
        SN["🛡️ Sentinel<br/>(Integrity & Drift)"]
    end

    OR -.-> T1["Tier 1: Logic"]
    DM -.-> T2["Tier 2: Standards"]
    SN -.-> T3["Tier 3: Behavior"]
    SN -.-> T4["Tier 4: Execution"]
```

### 👁️ Role 00: Chronos-Oracle (Strategic Memory)
- **Integration**: Operates in **01-Strategic-Nexus**.
- **Duty**: Analyzes session logs and deployment history to identify "Architectural Amnesia." It focuses on the **"Why"** behind decisions to prevent recurring debates and reasoning drift.

### 🛡️ Role 09: Sentinel (Integrity Auditor)
- **Integration**: Injected during the **Preflight Check** (`start_squad.py`).
- **Duty**: Acts as the "Border Control." It runs the `Brain-Health-Audit` to ensure that no mission starts if the KMS is in a state of drift or incoherence.

### 🧹 Role 05: DocMaintainer (Knowledge Health)
- **Integration**: Operates on the **Connective Tissue** of the vault.
- **Duty**: Scans for broken links, missing metadata, and tag dilution. It ensures that the "Semantic Graph" remains navigable for both humans and other AI agents.

---
> [!TIP]
> Always start your session by reading the **[[Ecosystem-Map-MOC]]** to see the current fleet health and active tasks.

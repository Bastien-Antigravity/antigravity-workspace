---
microservice: obsidian-brain
type: documentation
status: active
tags:
- \'#zone/3-fleet\'
- \'#service/obsidian-brain\'
- "#type/documentation"
- "#state/active"
---

# 🧠 Obsidian Brain: Features & Behavior

The `obsidian-brain` repository serves as the **Global Memory** and **Strategic Command Center** for the entire Bastien-Antigravity ecosystem. It orchestrates AI agents, manages behavioral specifications, and dictates architectural standards.

## 🗺️ Core Architecture & Behavior Mind Map

```mermaid
mindmap
  root((Obsidian Brain))
    Command & Control
      AI Orchestration
        AI Squad & Agents
        Prompts & Rules
      Scripts
        start_squad
        switch_mode
    The 3-Zone Architecture
      Zone 1 Frozen
        Business BDD Specs
        Source of Truth
      Zone 2 Fluid
        Rapid Prototyping
        Labs & Experiments
      Zone 3 Fleet
        Fleet Operations
        Global Action Plans
    Knowledge Management
      Tech Stack Rules
        Architecture Standards
        Coding Guidelines
      Core KMS
        5D Paradigm
        Tag Taxonomy
      State & Tasks
        Sprint Dashboards
        Domain Ontology
    Strategic Nexus
      Chronos Oracle
      Strategy Audit
```

## 🔄 Knowledge Flow (The 5D Paradigm)

This graph illustrates how knowledge flows and governs the ecosystem:

```mermaid
flowchart TD
    %% Zones
    Z1["❄️ Zone 1: Frozen\n(02-Business-BDD)"]:::frozen
    Z2["🧪 Zone 2: Fluid\n(04-Rapid-Prototyping)"]:::fluid
    Z3["🛰️ Zone 3: Fleet\n(05-Fleet-Operation)"]:::fleet
    
    %% Governance
    Gov["🏛️ Governance & Standards\n(03-Tech-Stack & 00-AI-Orchestration)"]:::gov
    
    %% Execution
    Exe["💻 Sandbox & Microservices\n(Code execution)"]:::exe

    Gov -->|Dictates Rules| Z1
    Gov -->|Dictates Rules| Z2
    Gov -->|Dictates Rules| Z3
    
    Z2 -->|Validates Idea| Z1
    Z1 -->|Generates Spec| Exe
    Exe -->|Deployed to| Z3

    classDef frozen fill:#e0f7fa,stroke:#00acc1,stroke-width:2px,color:#000;
    classDef fluid fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000;
    classDef fleet fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#000;
    classDef gov fill:#fce4ec,stroke:#5e35b1,stroke-width:2px,color:#000;
    classDef exe fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000;
```

## 🎯 Key Behaviors

1. **Multi-Mode Engine**: Operates in different protocols (Spec-First, Labs, Fleet) to balance stability with speed.
2. **AI Agent Delegation**: Uses specialized subagents (Architect, Sentinel, Developer, Oracle, QA, DocMaintainer) to enforce standards and isolate operational context.
3. **Behavior-Driven Quality**: Enforces that all execution code must stem from a BDD specification in `02-Business-BDD` and be tested in the `sandbox-testing` hub.
4. **Zettelkasten Connectivity**: Utilizes atomic notes, dynamic tracking (via Dataview), and Maps of Content (MOCs) to maintain a highly connected, easily navigable strategic graph.

---
microservice: obsidian-brain
type: governance
status: active
tags:
- '#type/governance'
- '#state/active'
- '#zone/3-fleet'
- '#service/obsidian-brain'
---
# 🧬 Project DNA: obsidian-brain

## 🎯 High-Level Intent (BDD)
- **Goal**: Serve as the "Global Memory" and "Strategic Command Center" for the entire Bastien-Antigravity ecosystem, housing all architectural decisions, sprint plans, and cross-repo knowledge.
- **Key Pattern**: **Atomic Knowledge** (Zettelkasten-style notes) and **Strategic MOCs** (Maps of Content for navigation).
- **Behavioral Source of Truth**: 02-Business-BDD/02-Behavior-Specs/obsidian-brain
- **Taxonomy Mandate**: Mandatory use of `#service/`, `#tech/`, `#tier/`, and `#zone/` tags for transversal concepts.
- **Isolation Protocol**: Human-centric documentation must reside in `quick-overview/` folders and carry the `#ai/ignore` tag.

## 🛠️ Role Specifics
- **FleetArchitect**: 
    - Maintain the integrity of the `Knowledge-Strategy.md` and `Ecosystem-Map-MOC.md`.
    - Ensure that submodules (`01-Strategic-Nexus`, `07-Core-KMS`, `03-Tech-Stack`, `02-Business-BDD`, `05-Fleet-Operation`, `04-Rapid-Prototyping`) are synchronized.
- **Orchestrator**: 
    - Act as the central "Pipeline Director."
    - Score task complexity (Fast-Track vs Standard) and route to downstream roles.
- **FleetCommander**: 
    - Manage the synchronization and deployment of the entire fleet.
    - Enforce compliance before all git pushes using `fleet-manager.py`.
- **DocMaintainer**:
    - Manage the **Isolation Protocol** and frontmatter integrity across the fleet.
    - Automate the injection of `#service/` tags.
- **Sentinel**: 
    - Run `Brain-Health-Audit.py` to verify link integrity and YAML compliance.
    - Audit the `AI-Session-State` consistency across repositories.
- **Purger**:
    - Periodically identify and remove legacy files, orphaned drafts, and technical debt.
- **Oracle (Chronos-Oracle)**:
    - Perform **Log-Driven Strategic Synthesis** by default at the start of every session.
    - Maintain the `01-Strategic-Nexus/` vault and the **Anti-Backlog**.
- **Developer**:
    - Follow the PARA/Diátaxis hybrid organizational system.
- **Architect**:
    - Design decoupled system interfaces and blueprints, performing Mode 1 design verification gates.
- **QA**:
    - Design BDD Gherkin test scenarios and sandbox execution skeletons before coding, verifying exit pass gates.
- **DocIndexer**:
    - Specialize in parsing, tokenizing, and indexing markdown files into the hybrid lexical/vector storage.
- **CodeIndexer**:
    - Specialize in AST-based code analysis, chunking, and code dependency index management.
- **PatternSentinel**:
    - Audit changes to enforce strict governance protocols, decoupling, and coding style standards.

## 🚦 Lifecycle & Versioning
- **Primary Branch**: `develop`
- **Protected Branches**: `main`
- **Versioning Strategy**: N/A (Continuous updates).
- **Version Source of Truth**: `VERSION.txt` (Set to `1.0.0` for tracking).


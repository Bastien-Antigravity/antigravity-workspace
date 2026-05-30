---
title: ARCHITECTURE - obsidian-brain
type: architecture
status: active
microservice: obsidian-brain
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#state/active'
- '#type/architecture'
---
# 🏗 Architecture: Obsidian Brain

## Overview
The **Obsidian Brain** is the central Knowledge Management System (KMS) and Strategic Command Center for the Bastien-Antigravity ecosystem.

## 3-Zone Architecture
1. **🛡️ Zone 1: Frozen (02-Business-BDD)**: Gherkin specs.
2. **🧪 Zone 2: Fluid (04-Rapid-Prototyping)**: Experiments.
3. **🛰️ Zone 3: Fleet (05-Fleet-Operation)**: Global Operations.

## Core Components
- **AI Orchestration (`00-AI-Orchestration`)**: Governance and initialization.
- **Strategic Nexus (`01-Strategic-Nexus`)**: High-level audits.
- **Core KMS (`07-Core-KMS`)**: Shared workflows and scripts.
- **RAG Engine (`09-RAG-Engine`)**: Semantic search capabilities.

## Data Flow
- **Knowledge**: Captured in Markdown, linked via MOCs.
- **Orchestration**: Driven by `start_squad.py` using personas.
- **Feedback**: Closed via `AI-Session-State.md`.

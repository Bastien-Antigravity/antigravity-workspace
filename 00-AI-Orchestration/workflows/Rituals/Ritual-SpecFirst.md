---
microservice: obsidian-brain
type: governance
status: active
tags:
- '#service/obsidian-brain'
- '#type/governance'
- '#state/active'
- '#zone/3-fleet'
---# 🛡️ Spec-First Rituals (Level 1)

These rules are MANDATORY when operating in **Mode 1**.

## 1. The Spec Gate
- **Draft First**: Before any code is written, you MUST transition to the **Spec Specialist** role.
- **BDD Requirement**: Draft or update a Gherkin-style spec in `02-Business-BDD/02-Behavior-Specs/`.
- **Approval**: Implementation cannot start until the spec has `status: approved`.

## 2. Purger Gate (Straight-to-Goal)
- **Simplify**: For every new feature, you MUST identify at least one opportunity to **Consolidate** or **Simplify** existing patterns.
- **Goal**: Minimize net complexity of the microservice.

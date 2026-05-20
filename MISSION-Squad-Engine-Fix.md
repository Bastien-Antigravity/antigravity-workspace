---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---# MISSION: Repair start_squad.py & Workflow Governance

## 🎯 Objective
Resolve critical functional conflicts, persona extraction failures, and governance inconsistencies within `start_squad.py` and its supporting script ecosystem (`20-Scripts/`).

## 🛠️ Scope
- **Critical Fixes (Priority 1):**
    - `protect_core_kms()` conflict with `Brain-Health-Audit.py`.
    - `persona_extractor.py` silent failure (menu/hooks).
    - `close_mission.py` push governance (branch check).
- **Governance Fixes (Priority 2):**
    - Sovereignty instance management (fix aggregate vs per-file reporting).
    - `_index_workspace()` directory pruning.
    - Double preflight execution.

## 👥 Assigned Specialist
**Sentinel** (Role: 09-Sentinel)

## 🏗️ Technical Requirements
- Ensure all fixes align with the existing `Sovereignty` engine architecture.
- Maintain consistency with the current `20-Scripts/` design patterns.
- **Verification:** Run a full engine lifecycle (launch, mission execute, sign-off) and confirm no regression in governance checks.

## 📝 Deliverables
- Patched `start_squad.py`, `close_mission.py`, and `persona_extractor.py`.
- Updated `install_git_hooks.py` to handle the persona extractor transition.
- Verification log in `AI-Session-State.md`.

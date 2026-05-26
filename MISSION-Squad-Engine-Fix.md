---
microservice: obsidian-brain
type: note
status: completed
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/completed'
- '#zone/3-fleet'
---# MISSION: Repair start_squad.py & Workflow Governance [COMPLETED]

## 🎯 Objective
Resolve critical functional conflicts, persona extraction failures, and governance inconsistencies within `start_squad.py` and its supporting script ecosystem (`20-Scripts/`).

## 🛠️ Scope
- **Critical Fixes (Priority 1):**
    - [x] `protect_core_kms()` conflict with `Brain-Health-Audit.py`. (Fixed by adding `unlock_core_kms()` before audit phase).
    - [x] `persona_extractor.py` silent failure (menu/hooks). (Main block enabled and path handling fixed).
    - [x] `close_mission.py` push governance (branch check). (Branch safety check added before git push).
- **Governance Fixes (Priority 2):**
    - [x] Sovereignty instance management (fix aggregate vs per-file reporting). (Per-file detailed reporting added to sign-off ritual).
    - [x] `_index_workspace()` directory pruning. (Added technical/temp folders to exclusion list).
    - [x] Double preflight execution. (Logic sequence cleaned and verified).

## 👥 Assigned Specialist
**Sentinel** (Role: 09-Sentinel)

## 🏗️ Technical Requirements
- Ensure all fixes align with the existing `Sovereignty` engine architecture.
- Maintain consistency with the current `20-Scripts/` design patterns.
- **Verification:** Run a full engine lifecycle (launch, mission execute, sign-off) and confirm no regression in governance checks.

## 📝 Deliverables
- [x] Patched `start_squad.py`, `close_mission.py`, and `persona_extractor.py`.
- [x] Updated `install_git_hooks.py` to handle the persona extractor transition. (Note: persona_extractor is now enabled as a background process).
- [x] Verification log in `AI-Session-State.md`.

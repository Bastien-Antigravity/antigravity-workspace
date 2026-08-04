---
microservice: obsidian-brain
type: governance
status: active
tags:
- '#service/obsidian-brain'
- '#type/governance'
- '#state/active'
- '#zone/3-fleet'
---# 🌎 Global AI Rituals (Level 0)

These rituals apply to ALL modes and sessions.

## 1. Starting the Session
1. **Restore State**: Read [[AI-Session-State]] and [[AI-Project-DNA]].
2. **Audit Environment**: Run `git branch --show-current` and check `VERSION.txt`. Verify they match the session state.
3. **Query Strategic Memory**: Proactively call the `query_strategic_decisions` tool to retrieve active Anti-Backlog constraints and Strategic Patterns to align with past architectural choices and avoid re-implementing rejected features.

## 2. AI Handover Protocol (State Machine)
To prevent context loss when switching roles, use the Inbox files:
- Update YAML: `status: active` -> `status: pending` and set `role: <next_role>`.
- The `Agent-Dispatcher.py` script will handle the transition.

## 3. Closing the Session
1. **Purger Phase**: Assumption of the **Purger** role. Delete any temporary files or obsolete scratchpads.
2. **Save State**: Update [[AI-Session-State]] with accurate progress.

## 4. The Wisdom Feedback Loop
1. **Extraction**: Ask: *"Did we learn a universal lesson today?"*
2. **Recording**: Update the relevant `Wisdom-Log.md` in the agent's `Role-Prompts/` folder.

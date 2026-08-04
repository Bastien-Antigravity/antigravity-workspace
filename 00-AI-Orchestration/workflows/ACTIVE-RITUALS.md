---
microservice: ecosystem-core
type: ritual
status: active
tags:
- '#zone/0-orchestration'
- '#tier/ritual'
- '#service/ecosystem-core'
- '#type/ritual'
- '#state/active'
---
# ⚡ ACTIVE SESSION RITUALS
> **Mode 1 Active** | Generated: 2026-07-11 17:16:05


# 🌎 Global AI Rituals (Level 0)

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


---

# 🛡️ Spec-First Rituals (Level 1)

These rules are MANDATORY when operating in **Mode 1**.

## 1. The Spec Gate
- **Draft First**: Before any code is written, you MUST transition to the **Spec Specialist** role.
- **BDD Requirement**: Draft or update a Gherkin-style spec in `02-Business-BDD/02-Behavior-Specs/`.
- **Approval**: Implementation cannot start until the spec has `status: approved`.

## 2. Purger Gate (Straight-to-Goal)
- **Simplify**: For every new feature, you MUST identify at least one opportunity to **Consolidate** or **Simplify** existing patterns.
- **Goal**: Minimize net complexity of the microservice.


---

# 🧠 STRATEGIC MEMORY (ACTIVE DECISIONS & PATTERNS)

> Do NOT re-implement or debate rejected features listed in the Anti-Backlog. Follow standard Strategic Patterns.

## ❌ The Anti-Backlog (Rejected Choices)
# 🚫 The Anti-Backlog

> "The historical record of conscious decisions NOT to implement a feature, pattern, or library."

## 🎯 Purpose
To prevent "Architectural Amnesia" where the same discarded ideas are re-debated every few months. If an idea is in the Anti-Backlog, it requires a significant change in ecosystem context to be reconsidered.

## 📁 Discarded Ideas

### 1. Direct Socket.io for Core Logging
- **Decision Date**: 2026-04-20
- **Reason**: Performance overhead and lack of memory safety in the node-js implementation for high-frequency logs.
- **Alternative**: Custom **SafeSocket** protocol over raw TCP.

### 2. Multi-Runtime FFI (Multiple Shared Libs)
- **Decision Date**: 2026-05-02
- **Reason**: Caused "Multiple Go Runtime" panics and memory isolation issues when Python/Rust loaded separate Go-based shared libraries.
- **Alternative**: The **Super-Bridge** (`universal-logger`).

### 3. Fragmented Knowledge Silos (PARA-only)
- **Decision Date**: 2026-05-16
- **Reason**: Caused "Reasoning Lag" and high token consumption due to excessive context-switching between 10+ repositories.
- **Alternative**: **Engineering-Brain Consolidation** (Merging Tech-Stack and Core-KMS).



---
*Reference: [[README]], [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Global-Architecture-Rules]]*



## 🛠️ Strategic Patterns (Proven Abstractions)
# 🧩 Strategic Patterns

> "Recurring architectural and operational truths that govern the Bastien-Antigravity ecosystem."

## 🏗️ Architectural Patterns
- **The Facade Law**: Core logic must always be wrapped in a language-agnostic facade (FFI/gRPC) to ensure polyglot compatibility.
- **Static Loading Law**: Binaries must be statically linked to avoid shared object hell in Docker environments.
- **The Super-Bridge**: Consolidated shared infrastructure (Logger + Config) into a single FFI boundary to prevent runtime panics.
- **Unified Logger and Config Parity**: All python services and scripts MUST use the `UniLog` and `AppConfig` modules from the `microservice-toolbox` package by default. Never fallback to standard Python logging or config libraries in production code. Dynamic library paths must be aligned at boot to prevent double Go runtime initialization on macOS.

## 🚀 Operational Patterns
- **Spec-First Enforcement**: Zero coding starts without an approved BDD spec.
- **Fail-Fast Security**: Reject unauthenticated or oversized payloads at the socket layer, not the application layer.
- **Atomic Fleet Actions**: If a multi-repo update fails on one repo, the entire action is halted for manual review.
- **The Sovereignty Ritual**: Mandatory Mission Sign-off and Git-aware stateless auditing before any fleet-wide merge.
- **Multi-AI Agnostic CLI**: All orchestration scripts must run on standard `python3` and avoid agent-specific syntax to ensure cross-platform/cross-AI compatibility.


---
*Reference: [[../README]], [[../archive/STRAT-001-The-Dormant-Pipeline|STRAT-001: The Dormant Pipeline]]*



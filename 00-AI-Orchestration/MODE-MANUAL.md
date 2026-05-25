---
microservice: obsidian-brain
title: 'AI Operating Manual: Multi-Mode Protocols'
version: 2.0
type: architecture
status: active
active_mode: 1
active_client: gemini
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#state/active'
- '#type/architecture'
---
# 🕹️ AI Operating Manual: Multi-Mode Protocols

This document defines the "Rules of Engagement" for the Antigravity AI assistant. By switching
between these modes, the USER can balance between **Safety (Specs)**, **Speed (Labs)**, and
**Scale (Orchestrator)**.

> [!IMPORTANT]
> Changing the mode changes the **Workflow**, not the **Brain**. All knowledge remains shared
> across all modes. The `active_mode` field in the header governs which protocol is active.

---

## 🛡️ Mode 1: Spec-First (The Governance Gate)

**Objective**: Maximum stability and zero-drift.
- **Rule 1**: No code changes without an approved BDD Spec in `02-Business-BDD/02-Behavior-Specs/`.
- **Rule 2**: Every fix must be audited against the spec before merging.
- **Rule 3**: Code cannot be merged until it strictly passes all Spec tests.
- **Rule 4**: At session end, the **FleetArchitect** must audit all configuration files of the modified repository, propose a commit message, and propose committing/pushing (with or without a Pull Request).
- **Rule 5**: Pre-session health audit: If any fleet repository is dirty (uncommitted changes), a large warning is shown requiring explicit user confirmation to proceed.
- **Rule 6**: **Pre-Task Checkpoint Mandate**: Before starting any new task, the agent MUST inspect the repository's git status. If uncommitted changes exist, the agent is strictly required to ask the user to commit or stash them first, preventing task inter-mixing and ensuring a safe rollback checkpoint.
- **Primary Brains**: `02-Business-BDD`, `03-Tech-Stack`
- **AI Persona**: **BrainSentinel** & **FleetArchitect** (Enforcing strict BDD compliance and architectural integrity).
- **Best For**: Core libraries, financial logic, and stable infrastructure.

---

## 🚀 Mode 2: Free-Labs (The Fast Path)

**Objective**: Rapid prototyping and experimental flow.
- **Rule 1**: BDD Specs are optional. Focus on speed and "MVP" (Minimum Viable Product).
- **Rule 2**: Work is isolated in `04-Rapid-Prototyping/`. Experiments are logged in
  `01-Experiment-Index/` using the experiment template.
- **Rule 3**: After a "Labs" feature is validated, perform a "Graduation Ceremony" — creating the BDD spec in `02-Business-BDD`, populating the `quick-overview/` docs via the **DocMaintainer**, and transitioning the code to Mode 1 standards.
- **Rule 4**: Special laboratory capabilities (cloning repository URLs, loading chat conversation URLs, URL exploration, and browser tool use with explicit user consent) are allowed, but STRICTLY RESTRICTED to Mode 2. They must never be executed in other modes.
- **Rule 5**: Pre-session health audit: If any fleet repository is dirty, a simple advisory warning message is shown.
- **Rule 6**: **Pre-Task Checkpoint Suggestion**: Before starting any new task, the agent should check git status and proactively suggest creating a lightweight checkpoint commit (e.g. `checkpoint: pre-[task]`) to enable easy rollback of experimental code.
- **Primary Brain**: `04-Rapid-Prototyping`
- **AI Persona**: **Developer** & **DocMaintainer** (Focused on fast iteration followed by documentation hardening).
- **Best For**: UI/UX design, new trading strategies, and one-off 20-Scripts.

---

## 🛰️ Mode 3: Agent Orchestrator (The Fleet Commander)

**Objective**: Scale and mass-execution.
- **Rule 1**: AI operates across multiple repositories simultaneously.
- **Rule 2**: Focus on "Fleet-Wide Action Plans" in
  `05-Fleet-Operation/01-Fleet-Action-Plans/` rather than individual lines of code.
- **Rule 3**: Automated testing is mandatory for every repo in the action plan.
- **Rule 4**: Before any push, the **FleetArchitect** must verify all GitHub configuration integrity (workflows, triggers, permissions, CODEOWNERS, settings) and block the push on any drift.
- **Rule 5**: Pre-session health audit: If any fleet repository is dirty, startup is strictly blocked, and the launcher will abort. The user must close/sign-off the active mission first.
- **Primary Brain**: `05-Fleet-Operation`
- **AI Persona**: **FleetCommander** (Focused on global architecture, synchronization, and ecosystem integrity).
- **Best For**: Global refactors, dependency updates, and release cycles.

---

## 🥷 Mode 4: Direct-Action (The Bypass)

**Objective**: Sporadic tasks and direct agent interaction without state overhead.
- **Rule 1**: Stateless execution. The global `active_mode` remains unchanged.
- **Rule 2**: No mandatory BDD or Sandbox tests (unless part of a specific sub-task).
- **Rule 3**: Best used for "Question & Answer" sessions, small script repairs, or one-off audits.
- **Rule 4**: **Discretionary Rollback Warning**: Before executing any code modifications, the agent must output a brief warning reminding the user to commit their current work locally, ensuring they can roll back easily since Mode 4 bypasses typical safety gates.
- **AI Persona**: Unified **Systems Engineer** (Default constraints).
- **Best For**: Quick README updates, link repairs in the vault, or "asking one agent a question."

---

## 🚦 The Switching Protocol

To switch modes, the USER must:
1. Say: `"Switch to Mode X"` (where X is 1, 2, or 3).
2. The AI will update `active_mode` in the YAML header of this file.
3. The AI will update `AI-Session-State.md` with: `Active Protocol: [[00-AI-Orchestration/MODE-MANUAL]]`.
4. The AI will announce:
   - Which **rules are activated** for this mode (e.g., Unified Systems Engineer).
   - Which **brains are primary** for this mode.
   - Which **constraints are relaxed or enforced**.

**Note on Mode 4**: This mode is typically activated via the `start_squad.py` CLI and does not require a global state change.

---

## 🔄 Mode Interaction Matrix

| Action | Mode 1 (Spec-First) | Mode 2 (Free-Labs) | Mode 3 (Fleet) | Mode 4 (Direct) |
|--------|---------------------|---------------------|-----------------|-----------------|
| BDD Spec required? | ✅ Mandatory | ❌ Optional | ✅ Per action plan | ❌ Optional |
| Sandbox tests? | ✅ Mandatory | ❌ Optional | ✅ Mandatory | ❌ Optional |
| Multi-repo ops? | ❌ Single repo | ❌ Single repo | ✅ Fleet-wide | ✅ Selective |
| Graduation needed? | N/A | ✅ To Mode 1 | N/A | N/A |
| AI Persona Focus | Strict Compliance | Rapid Iteration | Ecosystem Sync | Tactical Speed |
| Global State Update| ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |

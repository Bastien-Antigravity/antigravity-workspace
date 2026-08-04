---
microservice: obsidian-brain
type: documentation
status: active
tags:
- '#service/obsidian-brain'
- '#type/documentation'
- '#state/active'
- '#zone/3-fleet'
- role/human-onboarding
---
# AI Client Startup Guide

This guide explains how to start the AI Squad with Gemini and Codex.

The main entry point is:

```bash
python3 08-Base-Scripts/start_squad.py
```

Gemini is the default client. The client registry lives in `08-Base-Scripts/clients/registry.py`.

## Supported Clients

| Client | Runtime | Agent folder |
| --- | --- | --- |
| `gemini` | Native CLI | `.gemini/agents/` |
| `codex` | Native CLI | `.codex/agents/` |

## Start Commands

Run these from the `obsidian-brain` folder.

### Gemini

Gemini is the default:

```bash
python3 08-Base-Scripts/start_squad.py
```

Equivalent explicit form:

```bash
ACTIVE_CLIENT=gemini python3 08-Base-Scripts/start_squad.py
```

### Codex

```bash
ACTIVE_CLIENT=codex python3 08-Base-Scripts/start_squad.py
```

Requires the `codex` CLI to be installed and available in `PATH`.

```bash
ACTIVE_CLIENT=codex python3 08-Base-Scripts/start_squad.py
```

Requires the `codex` CLI to be installed and available in `PATH`.

## Client Selection

You can also set the default in `00-AI-Orchestration/Config/MODE-MANUAL.md`:

```yaml
active_client: gemini
```

## Setup Notes

Install vault-level Python dependencies:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

`start_squad.py` checks these dependencies at startup and installs missing packages into the active virtual environment.

## Agent Personas

Run `08-Base-Scripts/convert_agents.py` to regenerate all client-specific agent files:

```bash
python3 08-Base-Scripts/convert_agents.py
```

Generated folders:

- `.gemini/agents/`
- `.codex/agents/`

## RAG And MCP

Gemini and Codex can rely on their native client integrations where configured.

Expected RAG tools for native and API-driven clients:

- `query_brain`
- `get_brain_stats`
- `find_similar_files`
- `read_workspace_file`
- `write_workspace_file`
- `append_workspace_file`
- `list_workspace_directory`

## About `STATE LOG : MISSING`

This message comes from `08-Base-Scripts/close_mission.py`, not from the client startup itself.

It appears during the sign-off path when there are uncommitted Markdown changes but no changed `AI-Session-State.md` file in the same session payload.

Example:

```text
METADATA  : PASSED
STATE LOG : MISSING
VERDICT: MISSION BLOCKED
```

This usually means:

- The client started correctly.
- You exited through the mission sign-off path.
- The vault contains uncommitted Markdown changes.
- The session state was not updated before sign-off.

To resolve it, update `00-AI-Orchestration/AI-Session-State.md` with a short mission entry before signing off.

This is not a Gemini or Codex startup error. It is the governance gate enforcing session persistence.

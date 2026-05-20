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

This guide explains how to start the AI Squad with Gemini, Claude, Codex, or DeepSeek.

The main entry point is:

```bash
python3 20-Scripts/start_squad.py
```

Gemini is the default client. The client registry lives in `20-Scripts/clients/registry.py`.

## Supported Clients

| Client | Runtime | Agent folder |
| --- | --- | --- |
| `gemini` | Native CLI | `.gemini/agents/` |
| `claude` | Native CLI | `.claude/agents/` |
| `codex` | Native CLI | `.codex/agents/` |
| `deepseek` | API adapter | `.deepseek/agents/` |

## Start Commands

Run these from the `obsidian-brain` folder.

### Gemini

Gemini is the default:

```bash
python3 20-Scripts/start_squad.py
```

Equivalent explicit form:

```bash
ACTIVE_CLIENT=gemini python3 20-Scripts/start_squad.py
```

### Claude

```bash
ACTIVE_CLIENT=claude python3 20-Scripts/start_squad.py
```

Requires the `claude` CLI to be installed and available in `PATH`.

### Codex

```bash
ACTIVE_CLIENT=codex python3 20-Scripts/start_squad.py
```

Requires the `codex` CLI to be installed and available in `PATH`.

### DeepSeek

DeepSeek is API-backed:

```bash
ACTIVE_CLIENT=deepseek python3 20-Scripts/start_squad.py
```

It does not use a native DeepSeek MCP client. Instead, `20-Scripts/clients/API/deepseek_client.py` connects to the local RAG MCP server and bridges MCP tools to DeepSeek function calls.

You can also run the DeepSeek adapter directly:

```bash
python3 20-Scripts/clients/API/deepseek_client.py --mode 2 developer
```

## Client Selection

Preferred override:

```bash
ACTIVE_CLIENT=deepseek python3 20-Scripts/start_squad.py
```

Backward-compatible override:

```bash
ACTIVE_CLI=deepseek python3 20-Scripts/start_squad.py
```

You can also set the default in `00-AI-Orchestration/MODE-MANUAL.md`:

```yaml
active_client: gemini
```

## DeepSeek API Setup

Install vault-level Python dependencies:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

`start_squad.py` checks these dependencies at startup and installs missing packages into the active virtual environment.

Preferred setup is shell environment variables:

```bash
export DEEPSEEK_API_KEY="sk-..."
export DEEPSEEK_BASE_URL="https://api.deepseek.com"
export DEEPSEEK_MODEL="deepseek-chat"
```

`DEEPSEEK_BASE_URL` and `DEEPSEEK_MODEL` are optional. The defaults are:

```bash
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

The adapter also supports local `.env` files as a development fallback, but shell variables are preferred because they do not write secrets into the vault.

## Agent Personas

Run `20-Scripts/convert_agents.py` to regenerate all client-specific agent files:

```bash
python3 20-Scripts/convert_agents.py
```

Generated folders:

- `.gemini/agents/`
- `.claude/agents/`
- `.codex/agents/`
- `.deepseek/agents/`

## RAG And MCP

Gemini, Claude, and Codex can rely on their native client integrations where configured.

DeepSeek is different because it is an API, not a native local MCP client. The DeepSeek adapter starts the local RAG MCP server over stdio, converts the MCP tools into OpenAI-compatible tool schemas, executes requested tool calls locally, and sends the results back to the DeepSeek model.

Expected DeepSeek RAG tools:

- `query_brain`
- `get_brain_stats`
- `find_similar_files`
- `read_workspace_file`
- `write_workspace_file`
- `append_workspace_file`
- `list_workspace_directory`

## About `STATE LOG : MISSING`

This message comes from `20-Scripts/close_mission.py`, not from the client startup itself.

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

This is not a DeepSeek, Gemini, Claude, or Codex startup error. It is the governance gate enforcing session persistence.

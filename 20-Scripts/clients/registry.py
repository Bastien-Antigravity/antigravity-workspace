#!/usr/bin/env python
# coding:utf-8

"""
Central registry for supported Bastien-Antigravity AI clients.
"""

from __future__ import annotations

import os
import sys
from os.path import abspath, dirname, exists, join
from shutil import which
from typing import Dict, Iterable, List, Optional

SCRIPT_DIR = dirname(dirname(abspath(__file__)))
VAULT_ROOT = abspath(join(SCRIPT_DIR, ".."))

DEFAULT_CLIENT = "gemini"

CLIENTS: Dict[str, Dict[str, str]] = {
    "gemini": {
        "label": "Gemini",
        "kind": "cli",
        "command": "gemini",
        "agents_dir": ".gemini/agents",
    },
    "claude": {
        "label": "Claude",
        "kind": "cli",
        "command": "claude",
        "agents_dir": ".claude/agents",
    },
    "codex": {
        "label": "OpenAI Codex",
        "kind": "cli",
        "command": "codex",
        "agents_dir": ".codex/agents",
    },
    "deepseek": {
        "label": "DeepSeek",
        "kind": "api",
        "script": "20-Scripts/clients/API/deepseek_client.py",
        "agents_dir": ".deepseek/agents",
        "env_key": "DEEPSEEK_API_KEY",
    },
}


def client_names() -> List[str]:
    """Return supported client names in fallback order."""
    return list(CLIENTS.keys())


def iter_clients() -> Iterable[tuple[str, Dict[str, str]]]:
    """Yield supported client config entries in fallback order."""
    return CLIENTS.items()


def normalize_client(name: str) -> str:
    """Normalize aliases to registry names."""
    candidate = (name or "").strip().lower()
    aliases = {
        "openai": "codex",
        "chatgpt": "codex",
        "gpt": "codex",
    }
    return aliases.get(candidate, candidate)


def get_client_config(name: str) -> Optional[Dict[str, str]]:
    """Return a client config by normalized name."""
    return CLIENTS.get(normalize_client(name))


def get_agents_dir(vault_root: str, client_name: str) -> str:
    """Return the absolute agent directory for a client."""
    config = get_client_config(client_name)
    if not config:
        raise KeyError(f"Unsupported AI client: {client_name}")
    return join(vault_root, config["agents_dir"])


def list_agents(vault_root: str, client_name: str) -> List[str]:
    """List available markdown personas for a client."""
    agents_dir = get_agents_dir(vault_root, client_name)
    if not exists(agents_dir):
        return []
    try:
        return sorted(f[:-3] for f in os.listdir(agents_dir) if f.endswith(".md"))
    except OSError:
        return []


def is_client_available(client_name: str, vault_root: str) -> bool:
    """Check whether a client can be launched locally."""
    config = get_client_config(client_name)
    if not config:
        return False

    if config["kind"] == "cli":
        return which(config["command"]) is not None

    if config["kind"] == "api":
        script_path = join(vault_root, config["script"])
        return exists(script_path)

    return False


def build_launch_command(
    client_name: str,
    agent: str = "",
    squad_mode: str = "4",
    vault_root: str = VAULT_ROOT,
    python_executable: str = sys.executable,
) -> List[str]:
    """Build the subprocess command for a supported client."""
    config = get_client_config(client_name)
    if not config:
        raise ValueError(f"Unsupported AI client: {client_name}")

    if config["kind"] == "cli":
        command = [config["command"]]
        if agent:
            command.append(agent)
        return command

    if config["kind"] == "api":
        script_path = join(vault_root, config["script"])
        command = [
            python_executable,
            script_path,
            "--mode",
            "2",
            "--squad-mode",
            str(squad_mode),
        ]
        if agent:
            command.append(agent)
        return command

    raise ValueError(f"Unsupported client kind for {client_name}: {config['kind']}")

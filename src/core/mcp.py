#!/usr/bin/env python
# coding:utf-8

import os
import sys
import json
from typing import List, Dict, Any
from src.models.context import SystemContext

class MCPManager:
    """
    AI-CONTEXT: Manages MCP Server registration and configuration.
    Handles 'Firewall' logic (context exclusions) per mode.
    """
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx

    def configure_mcp(self) -> None:
        """Registers RAG or Filesystem MCP servers in AI client configs."""
        has_rag, rag_config = self._get_rag_config()
        mcp_args = None if has_rag else self._build_filesystem_args()
        
        configs = self._get_config_paths()
        for path, label in configs:
            self._update_config(path, label, has_rag, rag_config, mcp_args)

    def _get_rag_config(self) -> tuple[bool, Dict[str, Any]]:
        rag_dir = os.path.join(self.ctx.vault_root, "08-RAG-Engine")
        rag_script = os.path.join(rag_dir, "src", "core", "server.py")
        if not os.path.exists(rag_script):
            return False, {}

        # Resolve RAG Python
        local_python = os.path.join(rag_dir, ".venv", "Scripts", "python.exe" if os.name == "nt" else "bin/python3")
        
        # Fallback to vault-level .venv if local RAG venv is missing
        if not os.path.exists(local_python):
            vault_venv = os.path.join(self.ctx.vault_root, ".venv", "Scripts", "python.exe" if os.name == "nt" else "bin/python3")
            local_python = vault_venv if os.path.exists(vault_venv) else sys.executable
            
        return True, {
            "command": local_python,
            "args": [rag_script],
            "env": {
                "SQUAD_ACTIVE_MODE": str(self.ctx.active_mode),
                "PYTHONPATH": rag_dir
            }
        }

    def _build_filesystem_args(self) -> List[str]:
        global_excludes = {".obsidian", ".git", ".gemini", ".claude", ".codex", ".deepseek", "node_modules", "99-Humans", "quick-overview"}
        mode_excludes_map = {
            "1": {"01-Strategic-Nexus", "04-Rapid-Prototyping", "05-Fleet-Operation"},
            "2": {"01-Strategic-Nexus", "02-Business-BDD", "05-Fleet-Operation", "06-Microservices"},
            "3": {"01-Strategic-Nexus", "02-Business-BDD", "04-Rapid-Prototyping"},
            "4": set()
        }
        
        current_excludes = mode_excludes_map.get(self.ctx.active_mode, set())
        allowed_dirs = [self.ctx.workspace_root, self.ctx.vault_root]
        
        try:
            for item in os.listdir(self.ctx.vault_root):
                if item in global_excludes or item in current_excludes:
                    continue
                item_path = os.path.join(self.ctx.vault_root, item)
                if os.path.isdir(item_path):
                    allowed_dirs.append(item_path)
        except Exception: pass
        
        return ["-y", "@modelcontextprotocol/server-filesystem"] + allowed_dirs

    def _get_config_paths(self) -> List[tuple[str, str]]:
        home = os.path.expanduser("~")
        paths = [(os.path.join(home, ".gemini", "settings.json"), "Gemini")]
        if os.name == "nt":
            paths.append((os.path.join(os.getenv("APPDATA"), "Claude", "claude_desktop_config.json"), "Claude Win"))
        else:
            paths.append((os.path.join(home, "Library/Application Support/Claude", "claude_desktop_config.json"), "Claude Mac"))
        return paths

    def backup_settings(self) -> None:
        import shutil
        for path, label in self._get_config_paths():
            if os.path.exists(path):
                try:
                    shutil.copy2(path, path + ".bak")
                    print(f"📦 Created backup of {label} config")
                except Exception as e:
                    print(f"⚠️ Warning: Could not backup {label}: {e}")

    def restore_settings(self) -> None:
        import shutil
        for path, label in self._get_config_paths():
            bak_path = path + ".bak"
            if os.path.exists(bak_path):
                try:
                    shutil.move(bak_path, path)
                    print(f"📦 Restored original {label} from backup")
                except Exception as e:
                    print(f"⚠️ Warning: Could not restore {label}: {e}")

    def _update_config(self, path: str, label: str, has_rag: bool, rag_config: dict, fs_args: list) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        settings = {}
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
            except Exception: pass
            
        if "mcpServers" not in settings: settings["mcpServers"] = {}
        
        # Parity Cleanup
        settings["mcpServers"].pop("workspace_code_editor", None)
        
        if has_rag:
            settings["mcpServers"]["obsidian_rag"] = rag_config
            settings["mcpServers"].pop("obsidian_vault", None)
        else:
            settings["mcpServers"]["obsidian_vault"] = {"command": "npx", "args": fs_args}
            settings["mcpServers"].pop("obsidian_rag", None)
            
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2)
            print(f"✅ {label} MCP configured.")
        except Exception as e:
            print(f"⚠️ Could not write {label} config: {e}")

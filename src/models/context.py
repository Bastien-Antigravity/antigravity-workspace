#!/usr/bin/env python
# coding:utf-8

import os
import re
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

MODES = {
    "1": ("🛡️ Spec-First", "High safety, BDD mandatory."),
    "2": ("🧪 Free-Labs", "High speed, experimentations."),
    "3": ("🛰️ Fleet-Commander", "Global sync, multi-repo."),
    "4": ("🥷 Direct-Action", "Bypass mode logic.")
}

@dataclass
class SystemContext:
    """
    AI-CONTEXT: Encapsulates the state and configuration of the Orchestration Engine.
    Maintains 100% parity with legacy markdown-based state management.
    """
    vault_root: str
    workspace_root: str
    active_mode: str = "4"
    active_client: str = "gemini"
    
    # Internal paths
    orchestration_dir: str = field(init=False)
    mode_file: str = field(init=False)
    session_orch_file: str = field(init=False)
    session_root_file: str = field(init=False)
    inventory_file: str = field(init=False)
    
    # State
    mission_status: str = "parked"
    mission_id: str = "NONE"
    
    def __post_init__(self):
        self.orchestration_dir = os.path.join(self.vault_root, "00-AI-Orchestration")
        self.mode_file = os.path.join(self.orchestration_dir, "MODE-MANUAL.md")
        self.session_orch_file = os.path.join(self.orchestration_dir, "AI-Session-State.md")
        self.session_root_file = os.path.join(self.vault_root, "AI-Session-State.md")
        self.inventory_file = os.path.join(self.vault_root, "05-Fleet-Operation", "00-Repo-Control", "inventory.json")
        self.refresh()

    def refresh(self):
        """Reloads state from the markdown files to ensure parity."""
        self.active_mode = self._read_mode()
        self.active_client = self._read_active_client()
        self.mission_status, self.mission_id = self._read_mission_state()

    def _read_mode(self) -> str:
        if not os.path.exists(self.mode_file):
            return "4"
        try:
            with open(self.mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("active_mode:"):
                        return line.split(":")[1].strip()
        except Exception:
            pass
        return "4"

    def _read_mission_state(self) -> Tuple[str, str]:
        status, mid = "parked", "NONE"
        target = self.session_orch_file if os.path.exists(self.session_orch_file) else self.session_root_file
        if not os.path.exists(target):
            return status, mid
            
        try:
            with open(target, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("status:"):
                        status = line.split(":")[1].strip()
                    if line.startswith("Mission-ID:"):
                        mid = line.split(":")[1].strip()
        except Exception:
            pass
        return status, mid

    def _read_active_client(self) -> str:
        client = "gemini"
        if os.path.exists(self.mode_file):
            try:
                with open(self.mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip().startswith("active_cli:") or line.strip().startswith("active_client:"):
                            return line.split(":", 1)[1].strip().lower().replace("'", "").replace('"', '')
            except Exception:
                pass
        
        # Environment overrides
        for env_name in ("ACTIVE_CLIENT", "ACTIVE_CLI"):
            env_val = os.getenv(env_name)
            if env_val:
                return env_val.lower()
        
        return client

    def switch_mode(self, choice: str) -> bool:
        """Atomically updates all governance files (Parity with switch_mode.py)."""
        if choice not in MODES:
            return False

        # 1. Update MODE-MANUAL.md
        self._update_file_field(
            self.mode_file,
            r"active_mode:\s*\d+",
            f"active_mode: {choice}"
        )
        
        # 2. Update session states
        field_pattern = r'active-protocol:\s*[\'"].*?[\'"]'
        replacement = f'active-protocol: "[[MODE-MANUAL#Mode-{choice}]]"'
        
        self._update_file_field(self.session_orch_file, field_pattern, replacement)
        self._update_file_field(self.session_root_file, field_pattern, replacement)
        
        self.active_mode = choice
        return True

    def park_mission(self) -> bool:
        """Sets mission status to 'parked' in all governance files."""
        self._update_file_field(self.session_orch_file, r"status:\s*\w+", "status: parked")
        self._update_file_field(self.session_root_file, r"status:\s*\w+", "status: parked")
        self.mission_status = "parked"
        return True

    def start_mission(self, mission_id: str) -> bool:
        """Sets mission status to 'active' and updates Mission-ID."""
        self._update_file_field(self.session_orch_file, r"status:\s*\w+", "status: active")
        self._update_file_field(self.session_root_file, r"status:\s*\w+", "status: active")
        self._update_file_field(self.session_orch_file, r"Mission-ID:\s*.*", f"Mission-ID: {mission_id}")
        self._update_file_field(self.session_root_file, r"Mission-ID:\s*.*", f"Mission-ID: {mission_id}")
        self.mission_status = "active"
        self.mission_id = mission_id
        return True

    def _update_file_field(self, file_path: str, pattern: str, replacement: str) -> bool:
        if not os.path.exists(file_path):
            return False
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False

    @property
    def mode_name(self) -> str:
        return MODES.get(self.active_mode, ("Unknown", ""))[0]

    @property
    def mode_desc(self) -> str:
        return MODES.get(self.active_mode, ("", "Unknown"))[1]

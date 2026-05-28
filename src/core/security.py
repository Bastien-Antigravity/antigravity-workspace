#!/usr/bin/env python
# coding:utf-8

import os
from typing import List, Set, Optional
from src.models.context import SystemContext

class AccessController:
    """
    AI-CONTEXT: Security Middleware for the Bastien-Antigravity AI Squad.
    Enforces directory isolation and write protection based on the active mode.
    """
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx
        self.protected_patterns = {".git", ".obsidian", ".gemini", ".claude", ".codex", ".deepseek"}
        self.governance_dirs = {"07-Core-KMS", "00-AI-Orchestration"}

    def is_path_allowed(self, path: str, operation: str = "read") -> tuple[bool, str]:
        """
        Validates if an operation (read/write) is allowed on a path.
        Returns (is_allowed, reason).
        """
        abs_path = os.path.abspath(path)
        
        # 1. Protect core governance folders from modification
        if operation == "write":
            for gov in self.governance_dirs:
                if gov in abs_path:
                    return False, f"CRITICAL: Direct modification of governance zone ({gov}) is blocked."

        # 2. Protect sensitive metadata folders
        for pattern in self.protected_patterns:
            if pattern in abs_path:
                return False, f"SECURITY: Access to metadata folder ({pattern}) is restricted."

        # 3. Mode-Specific Isolation
        mode = self.ctx.active_mode
        
        if mode == "1": # Spec-First (Single Repo)
            # In Mode 1, we only allow access to the vault or the current working repo
            # (Simplification for now: assume vault access is always OK)
            if not abs_path.startswith(self.ctx.vault_root) and not abs_path.startswith(os.getcwd()):
                return False, "MODE 1: Operation outside current vault/repo is blocked. Switch to Mode 3 for multi-repo ops."

        elif mode == "2": # Free-Labs
            # Allow experimental paths
            pass

        elif mode == "3": # Fleet Commander
            # Multi-repo operations are allowed
            pass
            
        return True, "Allowed"

    def filter_file_list(self, files: List[str]) -> List[str]:
        """Filters out sensitive or restricted files from a list."""
        return [f for f in files if self.is_path_allowed(f, "read")[0]]

# coding:utf-8
"""
SHARED LIBRARY FOR SQUAD ORCHESTRATION PROCESSES
Contains common utilities for path resolution, terminal configuration, mode retrieval,
and fleet inventory management to eliminate code duplication across the ecosystem.
"""
import os
import sys
import json
from pathlib import Path
from typing import Tuple, List, Dict, Any

# ———————————————————————————————————————————————————————————————————————————————
# TERMINAL COLORS
# ———————————————————————————————————————————————————————————————————————————————
C_RESET = "\033[0m"
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_DIM = "\033[2m"
C_BOLD = "\033[1m"

# ———————————————————————————————————————————————————————————————————————————————
# SETUP FUNCTIONS
# ———————————————————————————————————————————————————————————————————————————————
def setup_terminal() -> None:
    """Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems."""
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except (AttributeError, Exception):
            pass

# ———————————————————————————————————————————————————————————————————————————————
# PATH & ECOSYSTEM RESOLUTION
# ———————————————————————————————————————————————————————————————————————————————
def resolve_vault_and_workspace(script_file: str) -> Tuple[Path, Path]:
    """
    Dynamically resolves the vault root (obsidian-brain) and workspace root (parent of vault).
    """
    current = Path(script_file).resolve().parent
    vault_root = None
    for parent in [current] + list(current.parents):
        if parent.name == "obsidian-brain":
            vault_root = parent
            break
            
    if not vault_root:
        # Fallback to parent of script dir if run directly from 08-Base-Scripts
        if current.name == "08-Base-Scripts" or current.name == "Scripts":
            vault_root = current.parent
        else:
            vault_root = current
            
    workspace_root = vault_root.parent
    return vault_root, workspace_root

# ———————————————————————————————————————————————————————————————————————————————
# GOVERNANCE & STATE OPERATIONS
# ———————————————————————————————————————————————————————————————————————————————
def get_active_mode(vault_root: Path) -> str:
    """
    Retrieves the currently selected active squad mode protocol from environment
    or fallback MODE-MANUAL.md.
    """
    mode = os.environ.get("SQUAD_ACTIVE_MODE")
    if mode:
        return mode
        
    mode_file = vault_root / "00-AI-Orchestration" / "MODE-MANUAL.md"
    if mode_file.exists():
        try:
            with open(mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("active_mode:"):
                        return line.split(":")[1].strip()
        except Exception:
            pass
    return "4"  # Default fallback mode

def get_fleet_repositories(vault_root: Path) -> List[Dict[str, Any]]:
    """
    Loads and returns the list of all registered repositories from inventory.json.
    """
    inventory_path = vault_root / "05-Fleet-Operation" / "00-Repo-Control" / "inventory.json"
    if not inventory_path.exists():
        return []
        
    try:
        with open(inventory_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("repositories", [])
    except Exception as e:
        sys.stderr.write(f"⚠️ Failed to load inventory.json: {e}\n")
        return []

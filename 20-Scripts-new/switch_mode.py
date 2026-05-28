#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Switches the operational protocol of the AI Squad by atomically updating
the MODE-MANUAL.md and all associated AI-Session-State.md files.

DATA FLOW:
1. Displays a selection UI for the available modes.
2. Resolves paths to 00-AI-Orchestration and root governance files.
3. Updates 'active_mode' in MODE-MANUAL.md.
4. Updates 'active-protocol' in both orchestration and root session states.

KEY PARAMETERS:
- MODES: Dict mapping numeric choices to (Name, Description) tuples.
"""
import os, sys
# Ensure we are running inside the virtual environment
_venv_dir = os.path.dirname(os.path.abspath(__file__))
while _venv_dir and _venv_dir != '/' and not os.path.exists(os.path.join(_venv_dir, ".venv")):
    _parent = os.path.dirname(_venv_dir)
    if _parent == _venv_dir:
        break
    _venv_dir = _parent
_venv_python = os.path.join(_venv_dir, ".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(_venv_dir, ".venv", "bin", "python3")
if os.path.exists(_venv_python):
    try:
        if not os.path.samefile(sys.executable, _venv_python):
            os.execl(_venv_python, _venv_python, *sys.argv)
    except OSError:
        pass


from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists
from re import sub as reSub, search as reSearch
from sys import stdout as sysStdout

# --- Configuration ---
MODES = {
    "1": ("🛡️ Spec-First", "High safety, BDD mandatory."),
    "2": ("🧪 Free-Labs", "High speed, experimentations."),
    "3": ("🛰️ Fleet-Commander", "Global sync, multi-repo."),
    "4": ("🥷 Direct-Action", "Bypass mode logic.")
}

# Standardize terminal output encoding for Windows
if sysStdout.encoding != 'utf-8':
    try:
        sysStdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# -----------------------------------------------------------------------------------------------

def _update_file_field(file_path: str, field_pattern: str, replacement: str) -> bool:
    """
    Updates a specific YAML field in a markdown file.
    Returns True if the field was found and updated.
    """
    if not osPathExists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = reSub(field_pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# -----------------------------------------------------------------------------------------------

def apply_mode_protocol(choice: str) -> bool:
    """
    ATOMALLY updates all governance files to the new protocol.
    Ensures zero drift between orchestration and root state logs.
    """
    if choice not in MODES:
        return False

    # Resolve paths relative to this script location
    script_dir = osPathDirname(osPathAbspath(__file__))
    orchestration_dir = osPathAbspath(osPathJoin(script_dir, "../00-AI-Orchestration"))
    
    mode_file = osPathJoin(orchestration_dir, "MODE-MANUAL.md")
    session_orch = osPathJoin(orchestration_dir, "AI-Session-State.md")
    session_root = osPathJoin(script_dir, "../AI-Session-State.md")
    
    if not osPathExists(mode_file):
        print(f"❌ Error: MODE-MANUAL.md not found at {mode_file}")
        return False

    # 1. Update MODE-MANUAL.md
    _update_file_field(
        mode_file,
        r"active_mode:\s*\d+",
        "active_mode: {0}".format(choice)
    )
    
    # 2. Atomically update BOTH AI-Session-State.md to match
    field_pattern = r'active-protocol:\s*[\'"].*?[\'"]'
    replacement = 'active-protocol: "[[MODE-MANUAL#Mode-{0}]]"'.format(choice)
    
    orch_synced = _update_file_field(session_orch, field_pattern, replacement)
    root_synced = _update_file_field(session_root, field_pattern, replacement)
    
    print(f"\n✅ SUCCESS: Protocol successfully set to: {MODES[choice][0]}")
    print(f"   AI-Session-State (Orch): {'Synced' if orch_synced else 'Already correct'}")
    print(f"   AI-Session-State (Root): {'Synced' if root_synced else 'Already correct'}")
    
    return True

# -----------------------------------------------------------------------------------------------

def get_mode_choice_interactive() -> str:
    """
    FUNCTIONAL ANALYSE:
    Displays the Selection UI and returns the validated choice.
    Returns None if the user skips selection.
    """
    print("\n--- 🕹️ Bastien-Antigravity: Mode Selector ---")
    for key, (name, desc) in MODES.items():
        print(f"[{key}] {name.ljust(18)} : {desc}")
    
    choice = input("\nSelect new active mode [1-4] (Enter to skip): ").strip()
    return choice if choice in MODES else None

# -----------------------------------------------------------------------------------------------

def main() -> None:
    """Entry point for standalone execution."""
    choice = get_mode_choice_interactive()
    if choice:
        apply_mode_protocol(choice)
    else:
        print("➡️ No changes made.")

if __name__ == "__main__":
    main()

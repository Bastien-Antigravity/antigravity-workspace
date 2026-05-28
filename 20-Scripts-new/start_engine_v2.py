#!/usr/bin/env python
# coding:utf-8

import os
import sys

# Ensure we can find the 'src' package
vault_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if vault_root not in sys.path:
    sys.path.append(vault_root)

# Resolve venv by walking up (parity with start_engine.py)
_venv_dir = vault_root
while _venv_dir and _venv_dir != os.path.dirname(_venv_dir) and not os.path.exists(os.path.join(_venv_dir, ".venv")):
    _venv_dir = os.path.dirname(_venv_dir)

# Check for virtual environment and re-exec if needed
_venv_python = os.path.join(_venv_dir, ".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(_venv_dir, ".venv", "bin", "python3")
if os.path.exists(_venv_python):
    try:
        if not os.path.samefile(sys.executable, _venv_python):
            os.execl(_venv_python, _venv_python, *sys.argv)
    except (OSError, ValueError):
        pass

try:
    from src import EngineFacade as SquadOrchestrator
except ImportError as e:
    print(f"❌ Error: Could not import OOP Core: {e}")
    sys.exit(1)

if __name__ == "__main__":
    orchestrator = SquadOrchestrator(vault_root)
    try:
        orchestrator.launch()
    except KeyboardInterrupt:
        print("\n👋 Forced exit. Session terminated.")
    sys.exit(0)

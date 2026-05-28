#!/usr/bin/env python3
# coding:utf-8
"""
🛡️ Git Hooks Installer
Installs background post-commit and post-merge hooks to keep RAG indexing 
and coding personas synchronized with Git repository updates automatically.
"""
import os
import sys
import stat

def install_hooks():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vault_root = os.path.abspath(os.path.join(script_dir, ".."))
    git_hooks_dir = os.path.join(vault_root, ".git", "hooks")
    
    if not os.path.exists(git_hooks_dir):
        print(f"❌ Error: Git hooks directory not found at {git_hooks_dir}. Make sure you are inside a Git repository.")
        sys.exit(1)
        
    hook_content = """#!/bin/sh
# Bastien-Antigravity Vault Git Hook
# Triggers RAG re-indexing and Persona Extraction asynchronously in the background.

cd "$(dirname "$0")/../.."

# Run RAG Indexer in the background
if [ -f "./08-RAG-Engine/.venv/bin/python3" ]; then
    PYTHONPATH="./08-RAG-Engine" ./08-RAG-Engine/.venv/bin/python3 ./08-RAG-Engine/main.py index > /dev/null 2>&1 &
elif [ -f "./08-RAG-Engine/.venv/Scripts/python.exe" ]; then
    PYTHONPATH="./08-RAG-Engine" ./08-RAG-Engine/.venv/Scripts/python.exe ./08-RAG-Engine/main.py index > /dev/null 2>&1 &
elif [ -f "./.venv/bin/python3" ]; then
    PYTHONPATH="./08-RAG-Engine" ./.venv/bin/python3 ./08-RAG-Engine/main.py index > /dev/null 2>&1 &
elif [ -f "./.venv/Scripts/python.exe" ]; then
    PYTHONPATH="./08-RAG-Engine" ./.venv/Scripts/python.exe ./08-RAG-Engine/main.py index > /dev/null 2>&1 &
else
    PYTHONPATH="./08-RAG-Engine" python3 ./08-RAG-Engine/main.py index > /dev/null 2>&1 &
fi

# Run Persona Extractor in the background
if [ -f "./.venv/bin/python3" ]; then
    ./.venv/bin/python3 ./20-Scripts/persona_extractor.py --daemon > /dev/null 2>&1 &
elif [ -f "./.venv/Scripts/python.exe" ]; then
    ./.venv/Scripts/python.exe ./20-Scripts/persona_extractor.py --daemon > /dev/null 2>&1 &
else
    python3 ./20-Scripts/persona_extractor.py --daemon > /dev/null 2>&1 &
fi
"""

    hooks = ["post-commit", "post-merge"]
    
    for hook in hooks:
        hook_path = os.path.join(git_hooks_dir, hook)
        try:
            with open(hook_path, 'w', encoding='utf-8') as f:
                f.write(hook_content)
            
            # Make the hook executable (chmod +x)
            st = os.stat(hook_path)
            os.chmod(hook_path, st.st_mode | stat.S_IEXEC)
            print(f"✅ Successfully installed {hook} hook at {hook_path}")
        except Exception as e:
            print(f"❌ Failed to install {hook} hook: {e}")

if __name__ == '__main__':
    install_hooks()

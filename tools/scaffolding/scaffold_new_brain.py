#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Scaffolds a new Bastien-Antigravity ecosystem directory by creating the 
standard folder structure and copying the AI Squad DNA.

DATA FLOW:
1. Inputs project name and destination path from user.
2. Creates the 2-Digit standard directory hierarchy.
3. Copies Role-Prompts and Scripts from the parent brain.
4. Generates initial README, GEMINI.md and MODE-MANUAL files.
5. Invokes convert_agents.py to initialize subagents.

KEY PARAMETERS:
- folders: List of standard directory names to create.
- target_path: The filesystem path where the new brain will be built.
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


from shutil import copytree as shutilCopytree, copy as shutilCopy
from subprocess import run as subprocessRun
from sys import executable as sysExecutable
from pathlib import Path

# -----------------------------------------------------------------------------------------------

def main() -> None:
    print("\n🏗️  Bastien-Antigravity: Ecosystem Scaffolder")
    print("-------------------------------------------")
    
    target_name = input("Enter new project name (e.g. quantum-finance): ").strip()
    if not target_name:
        print("❌ Error: Project name is required.")
        return
        
    target_path = Path(input(f"Enter destination path [default: ../{target_name}]: ").strip() or f"../{target_name}")
    
    if target_path.exists():
        print(f"❌ Error: Path {target_path} already exists.")
        return

    print(f"\n🚀 Fabricating '{target_name}' at {target_path.absolute()}...")

    # 1. Create Folder Structure
    folders = [
        "00-AI-Orchestration",
        "01-Strategic-Nexus",
        "02-Business-BDD",
        "03-Tech-Stack",
        "04-Rapid-Prototyping",
        "05-Fleet-Operation",
        "06-Microservices",
        "07-Core-KMS/Role-Prompts",
        "08-Base-Scripts",
        "99-Humans"
    ]
    
    for folder in folders:
        (target_path / folder).mkdir(parents=True, exist_ok=True)

    # 2. Copy "DNA" (Scripts and Role Prompts)
    current_dir = Path(__file__).resolve().parent.parent.parent
    
    print("🧬 Copying AI Squad DNA...")
    shutilCopytree(current_dir / "07-Core-KMS/Role-Prompts", target_path / "07-Core-KMS/Role-Prompts", dirs_exist_ok=True)
    shutilCopytree(current_dir / "08-Base-Scripts", target_path / "08-Base-Scripts", dirs_exist_ok=True)

    # 3. Create Template Files
    print("📝 Generating Project Compass...")
    
    # 🧬 AI-Project-DNA.md
    dna_content = f"""---
microservice: obsidian-brain
type: governance
status: active
---
# 🧬 AI Project DNA: {target_name}

## 🎯 High-Level Vision
Define the primary purpose of this brain here.

## 🛡️ Core Constraints
1. **The [SCAN] Protocol**: Every response must start with a [SCAN] block.
2. **Double-Digit Hierarchy**: Maintain the 00-99 folder structure.
3. **Isolation Zones**: Keep human dashboards in `99-Humans/` with `#ai/ignore`.
4. **Transversal Tags**: Every file must be classified via `#tech/`, `#tier/`, and `#zone/`.
"""
    with open(target_path / "00-AI-Orchestration/AI-Project-DNA.md", 'w', encoding='utf-8') as f:
        f.write(dna_content)

    # 🧠 AI-Session-State.md
    session_content = f"""---
microservice: obsidian-brain
type: state
status: active
active-protocol: "🛡️ Mode 1: Spec-First"
---
# 🧠 AI Session State: {target_name}

## 🚀 Active Missions
- [ ] Initialize the ecosystem.
"""
    with open(target_path / "00-AI-Orchestration/AI-Session-State.md", 'w', encoding='utf-8') as f:
        f.write(session_content)

    # ⚡ AI-Init.md
    init_content = f"""---
microservice: obsidian-brain
type: governance
status: active
---
# ⚡ AI Initialization: {target_name}

> [!IMPORTANT] MANDATORY INITIALIZATION
> Copy and paste this prompt when starting a new session:
> 
> "1. Read the ecosystem map in **[[Ecosystem-Map-MOC]]**."
> "2. Load project constraints from **[[AI-Project-DNA]]**."
> "3. Restore session state from **[[AI-Session-State]]**."
"""
    with open(target_path / "00-AI-Orchestration/AI-Init.md", 'w', encoding='utf-8') as f:
        f.write(init_content)

    # 🗺️ Ecosystem-Map-MOC.md
    moc_content = f"""---
microservice: ecosystem-core
type: moc
status: active
---
# 🌌 {target_name}: Master Knowledge Hub (MOC)

## 🤖 00 - AI Orchestration
- [[00-AI-Orchestration/AI-Project-DNA|🧬 AI Project DNA]]
- [[00-AI-Orchestration/AI-Init|⚡ AI Initialization]]
- [[00-AI-Orchestration/AI-Session-State|🧠 AI Session State]]
"""
    with open(target_path / "Ecosystem-Map-MOC.md", 'w', encoding='utf-8') as f:
        f.write(moc_content)

    with open(target_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(f"# 🧠 {target_name.replace('-', ' ').title()}\n\nNew Bastien-Antigravity Ecosystem.\n")

    # Copy User Manual
    if (current_dir / "User-Manual.md").exists():
        shutilCopy(current_dir / "User-Manual.md", target_path / "User-Manual.md")

    # 4. Initialize Mode Manual
    mode_content = "active_mode: 1\n\n# Mode Manual\n1: Spec-First\n2: Free-Labs\n3: Fleet-Commander\n"
    with open(target_path / "00-AI-Orchestration/MODE-MANUAL.md", 'w', encoding='utf-8') as f:
        f.write(mode_content)

    # 5. Run Agent Conversion in the new project
    print("🤖 Baking the AI Squad into the new ecosystem...")
    subprocessRun([sysExecutable, "08-Base-Scripts/convert_agents.py"], cwd=target_path)

    print(f"\n✅ SUCCESS! Your new Command Center is ready at: {target_path.absolute()}")
    print(f"👉 To start: cd {target_path} && {sysExecutable} 08-Base-Scripts/start_squad.py\n")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

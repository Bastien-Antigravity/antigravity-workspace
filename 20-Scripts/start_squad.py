#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Initializes the Bastien-Antigravity AI Squad Command Center. Handles MCP binding,
pre-session audits, role synchronization, and launches the Gemini CLI.

DATA FLOW:
1. Performs Preflight and Sovereignty audits to detect architecture drift.
2. Synchronizes Role-Prompts to agent definitions (convert_agents.py).
3. Invokes the Mode Selector and applies the protocol (switch_mode.py).
4. Configures the MCP server-filesystem based on mode isolation rules.
5. Launches the Gemini CLI in a re-launchable lifecycle loop.

KEY PARAMETERS:
- vault_root: Resolved path to the Obsidian Brain vault.
- mcp_args: Dynamic arguments for the filesystem MCP server.
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

from sys import executable as sysExecutable, path as sysPath, stdout as sysStdout, exit as sysExit
from os import makedirs as osMakedirs, listdir as osListdir, name as osName
from json import dump as jsonDump, load as jsonLoad
from subprocess import run as subprocessRun
from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists, \
                    expanduser as osPathExpanduser, isdir as osPathIsdir, basename as osPathBasename

# Add current directory to sys.path to enable library imports
script_dir = osPathDirname(osPathAbspath(__file__))
if script_dir not in sysPath:
    sysPath.append(script_dir)

try:
    from switch_mode import get_mode_choice_interactive, apply_mode_protocol, MODES
    from mission_help import MissionHelper
except ImportError:
    print("❌ Error: Could not find switch_mode.py or mission_help.py in 20-Scripts/")
    sysExit(1)

# Standardize terminal output encoding for Windows
if sysStdout.encoding != 'utf-8':
    try:
        sysStdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# -----------------------------------------------------------------------------------------------

def setup_mcp(mode_choice: str) -> None:
    """
    DATA FLOW:
    Resolves vault root and configures the MCP filesystem server.
    Implements the Isolation Protocol by excluding forbidden zones.
    """
    settings_dir = osPathExpanduser("~/.gemini")
    settings_file = osPathJoin(settings_dir, "settings.json")
    
    if not osPathExists(settings_dir):
        osMakedirs(settings_dir, exist_ok=True)
    
    settings = {}
    if osPathExists(settings_file):
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = jsonLoad(f)
        except Exception:
            print("⚠️ Warning: Corruption detected in settings.json. Starting fresh.")
    
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}
        
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    
    # --- Dynamic Context Exclusion Logic (The Firewall) ---
    global_excludes = {".obsidian", ".git", ".gemini", "node_modules", "99-Humans", "quick-overview"}
    mode_excludes_map = {
        "1": {"01-Strategic-Nexus", "04-Rapid-Prototyping", "05-Fleet-Operation"},
        "2": {"01-Strategic-Nexus", "02-Business-BDD", "05-Fleet-Operation", "06-Microservices"},
        "3": {"01-Strategic-Nexus", "02-Business-BDD", "04-Rapid-Prototyping"},
        "4": set()
    }
    
    current_excludes = mode_excludes_map.get(mode_choice, set())
    allowed_dirs = []
    
    for item in osListdir(vault_root):
        if item in global_excludes or item in current_excludes:
            continue
        item_path = osPathJoin(vault_root, item)
        if osPathIsdir(item_path):
            allowed_dirs.append(item_path)
        
    mcp_args = ["-y", "@modelcontextprotocol/server-filesystem"] + allowed_dirs
    
    settings["mcpServers"]["obsidian_vault"] = {
        "command": "npx",
        "args": mcp_args
    }
    
    with open(settings_file, 'w', encoding='utf-8') as f:
        jsonDump(settings, f, indent=2)
        
    print(f"✅ MCP Context Boundary defined. Vault bound: {vault_root}")

# -----------------------------------------------------------------------------------------------

def run_preflight() -> None:
    """
    ESSENTIAL PROCESS:
    Runs the full audit chain to ensure the brain is healthy before session start.
    """
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    
    # Candidates for Preflight and Audit scripts
    scripts = [
        osPathJoin(workspace_root, "core-kms-brain", "Scripts", "Preflight-Check.py"),
        osPathJoin(script_dir, "../07-Core-KMS/Scripts/Preflight-Check.py"),
        osPathJoin(workspace_root, "core-kms-brain", "Scripts", "Brain-Health-Audit.py"),
        osPathJoin(script_dir, "../07-Core-KMS/Scripts/Brain-Health-Audit.py")
    ]
    
    for script in scripts:
        if osPathExists(script):
            print(f"📡 Executing Governance Audit: {osPathBasename(script)}...")
            subprocessRun([sysExecutable, script])

def check_session_health() -> None:
    """
    Checks if there are uncommitted changes from a previous session.
    Ensures the mission was properly closed.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    try:
        result = subprocessRun(
            ["git", "status", "--porcelain"], 
            cwd=vault_root, capture_output=True, text=True, check=True
        )
        uncommitted = [line for line in result.stdout.splitlines() if line.strip().endswith(".md")]
        
        if uncommitted:
            print("\n" + "!"*60)
            print("⚠️  UNCLOSED MISSION DETECTED")
            print(f"There are {len(uncommitted)} uncommitted markdown files in the vault.")
            print("Please run 'python3 20-Scripts/close_mission.py' to verify and sign-off.")
            print("!"*60 + "\n")
            
            confirm = input("Ignore and start new session anyway? [y/N]: ").lower().strip()
            if confirm != 'y':
                print("👋 Session aborted. Please close the previous mission first.")
                sysExit(0)
    except Exception:
        pass # Git not found or other error

def regenerate_agents() -> None:
    """
    DATA FLOW:
    Triggers the multi-AI agent converter to ensure prompts are synchronized.
    """
    convert_script = osPathJoin(script_dir, "convert_agents.py")
    if osPathExists(convert_script):
        print("🔄 Synchronizing AI Squad Roles across adapters...")
        subprocessRun([sysExecutable, convert_script])

# -----------------------------------------------------------------------------------------------

def start_engine() -> None:
    """
    FUNCTIONAL ANALYSE:
    Implements the Master Lifecycle Loop. This allows the user to re-launch
    the engine or switch modes without manually restarting the script.
    """
    while True:
        print("\n" + "="*60)
        print("🧠 BASTIEN-ANTIGRAVITY: AI SQUAD COMMAND")
        print("="*60)

        # 1. Verification & Sync
        check_session_health()
        run_preflight()
        regenerate_agents()

        # 2. Mode Management
        choice = get_mode_choice_interactive()
        if choice:
            apply_mode_protocol(choice)
        else:
            # Re-read current mode if skip
            choice = "4"
            mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
            if osPathExists(mode_file):
                with open(mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith("active_mode:"):
                            choice = line.split(":")[1].strip()
                            break
        
        # 3. Protocol Enforcement
        setup_mcp(choice)
        
        # 4. Display Mission Guidance
        helper = MissionHelper()
        helper.print_cheat_sheet()
        
        # 5. CLI Execution
        clis = ["gemini", "claude", "codex", "mistral", "deepseek"]
        active_cli = "gemini" # Default
        
        # Simple detection (in a real scenario, we could check which is in PATH)
        print(f"\n🚀 Firing up the AI Squad Command [Protocol: {choice}]...")
        
        try:
            # Check for Windows or Unix
            cmd_prefix = [] if osName != 'nt' else ["cmd", "/c"]
            
            # Execute the primary CLI
            subprocessRun(cmd_prefix + [active_cli])
        except FileNotFoundError:
            print(f"⚠️ Warning: {active_cli} CLI not found. Trying fallback CLIs...")
            for fallback in clis[1:]:
                try:
                    subprocessRun(cmd_prefix + [fallback])
                    break
                except FileNotFoundError:
                    continue
        except Exception as e:
            print(f"❌ CLI Execution Error: {e}")
            break
            
        # 6. Lifecycle Decision
        print("\n--- 🏁 Session Paused ---")
        decision = input("Re-launch Squad? [y: Yes / n: Exit & Sign-off / s: Switch Mode]: ").lower().strip()
        
        if decision == 's' or decision == 'y':
            continue
        else:
            print("\n📡 Initiating Mission Sign-off Ritual...")
            signoff_script = osPathJoin(script_dir, "close_mission.py")
            if osPathExists(signoff_script):
                subprocessRun([sysExecutable, signoff_script])
            print("👋 Squad resting. Mission concluded.")
            break

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
        sysExit(0)

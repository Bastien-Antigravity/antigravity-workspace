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
    Resolves vault root and configures the MCP filesystem and RAG servers.
    Registers servers in both Gemini and Claude configurations dynamically (AI-agnostic).
    Allows root access to fix 'path not allowed' errors for Ecosystem Map and manuals.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    workspace_root = osPathAbspath(osPathJoin(vault_root, ".."))
    
    # 1. Check if RAG Engine option is available
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "server.py")
    has_rag = osPathExists(rag_dir) and osPathExists(rag_server_script)
    
    obsidian_rag_config = None
    mcp_args = None
    
    if has_rag:
        # Determine the Python virtual environment path dynamically:
        # 1. If local 08-RAG-Engine/.venv exists, use it (contains specific RAG packages).
        # 2. Otherwise, fallback to the central obsidian-brain/.venv.
        local_venv = osPathJoin(rag_dir, ".venv")
        local_python = osPathJoin(local_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(local_venv, "bin", "python3")
        
        if osPathExists(local_python):
            resolved_python = local_python
            print(f"📡 RAG using local 08-RAG-Engine virtual environment: {resolved_python}")
        else:
            parent_venv = osPathJoin(vault_root, ".venv")
            parent_python = osPathJoin(parent_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(parent_venv, "bin", "python3")
            resolved_python = parent_python
            print(f"📡 RAG using central obsidian-brain virtual environment: {resolved_python}")
            
        obsidian_rag_config = {
            "command": resolved_python,
            "args": [rag_server_script],
            "env": {
                "SQUAD_ACTIVE_MODE": str(mode_choice)
            }
        }
    else:
        # Fallback to standard basic filesystem MCP server
        # --- Dynamic Context Exclusion Logic (The Firewall) ---
        global_excludes = {".obsidian", ".git", ".gemini", "node_modules", "99-Humans", "quick-overview"}
        mode_excludes_map = {
            "1": {"01-Strategic-Nexus", "04-Rapid-Prototyping", "05-Fleet-Operation"},
            "2": {"01-Strategic-Nexus", "02-Business-BDD", "05-Fleet-Operation", "06-Microservices"},
            "3": {"01-Strategic-Nexus", "02-Business-BDD", "04-Rapid-Prototyping"},
            "4": set()
        }
        
        current_excludes = mode_excludes_map.get(mode_choice, set())
        allowed_dirs = [workspace_root, vault_root]
        
        try:
            for item in osListdir(vault_root):
                if item in global_excludes or item in current_excludes:
                    continue
                item_path = osPathJoin(vault_root, item)
                if osPathIsdir(item_path):
                    allowed_dirs.append(item_path)
        except Exception as e:
            print(f"⚠️ Warning: Could not scan vault_root for exclusions: {e}")
                
        mcp_args = ["-y", "@modelcontextprotocol/server-filesystem"] + allowed_dirs
    
    # 2. Update MCP configs (AI-Agnostic: Gemini and Claude)
    configs_to_update = [
        # (filepath, label)
        (osPathJoin(osPathExpanduser("~/.gemini"), "settings.json"), "Gemini Settings"),
    ]
    if osName != "nt":  # Claude desktop is Mac/Windows, but on Mac we definitely expand it
        configs_to_update.append(
            (osPathJoin(osPathExpanduser("~/Library/Application Support/Claude"), "claude_desktop_config.json"), "Claude Settings")
        )
    else:
        configs_to_update.append(
            (osPathJoin(osPathExpanduser("~/AppData/Roaming/Claude"), "claude_desktop_config.json"), "Claude Settings Windows")
        )
        
    for config_file, label in configs_to_update:
        config_dir = osPathDirname(config_file)
        if not osPathExists(config_dir):
            try:
                osMakedirs(config_dir, exist_ok=True)
            except Exception:
                continue # Skip if directory cannot be created
                
        settings = {}
        if osPathExists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    settings = jsonLoad(f)
            except Exception:
                print(f"⚠️ Warning: Corruption detected in {label}. Starting fresh.")
                
        if "mcpServers" not in settings:
            settings["mcpServers"] = {}
            
        # Clean up old workspace_code_editor name
        settings["mcpServers"].pop("workspace_code_editor", None)
        
        if has_rag:
            # Unified RAG Server: register it, clean up standard filesystem MCP
            settings["mcpServers"]["obsidian_rag"] = obsidian_rag_config
            settings["mcpServers"].pop("obsidian_vault", None)
        else:
            # Fallback standard filesystem server: register it, clean up RAG
            settings["mcpServers"]["obsidian_vault"] = {
                "command": "npx",
                "args": mcp_args
            }
            settings["mcpServers"].pop("obsidian_rag", None)
            
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                jsonDump(settings, f, indent=2)
            print(f"✅ {label} configured successfully.")
        except Exception as e:
            print(f"⚠️ Warning: Could not write {label}: {e}")

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
    # Exclude internal folders, templates, and programmatic manuals from the mandatory audit
    EXCLUSIONS = [".git", ".obsidian", ".gemini", "Templates", "MODE-MANUAL.md"]
    try:
        result = subprocessRun(
            ["git", "status", "--porcelain"], 
            cwd=vault_root, capture_output=True, text=True, check=True
        )
        uncommitted = []
        for line in result.stdout.splitlines():
            status_path = line[3:].strip()
            if status_path.endswith(".md"):
                if any(x in status_path for x in EXCLUSIONS):
                    continue
                uncommitted.append(status_path)
        
        if uncommitted:
            print("\n" + "!"*60)
            print("⚠️  UNCLOSED MISSION DETECTED")
            print(f"There are {len(uncommitted)} uncommitted markdown files in the vault.")
            print("Please run 'python3 ./obsidian-brain/20-Scripts/close_mission.py' to verify and sign-off.")
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

def protect_core_kms() -> None:
    """
    Sets the 07-Core-KMS directory and files to read-only
    at the OS level to protect them against modifications.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    kms_dir = osPathJoin(vault_root, "07-Core-KMS")
    if not osPathExists(kms_dir):
        return
    print("🔒 Enforcing read-only permissions on 07-Core-KMS directory...")
    for root, dirs, files in os.walk(kms_dir):
        for d in dirs:
            dir_path = osPathJoin(root, d)
            try:
                os.chmod(dir_path, 0o555)
            except Exception:
                pass
        for f in files:
            file_path = osPathJoin(root, f)
            try:
                os.chmod(file_path, 0o444)
            except Exception:
                pass

def check_rag_attached() -> bool:
    """Returns True if the 08-RAG-Engine and its server.py exist."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "server.py")
    return osPathExists(rag_dir) and osPathExists(rag_server_script)

def reset_rag_index() -> None:
    """
    DATA FLOW:
    Resolves the RAG virtual environment python executable and runs indexer.py --reset.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    indexer_script = osPathJoin(rag_dir, "src", "indexer.py")
    
    if not osPathExists(indexer_script):
        print("❌ Error: indexer.py not found. Cannot reset RAG index.")
        return
        
    local_venv = osPathJoin(rag_dir, ".venv")
    local_python = osPathJoin(local_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(local_venv, "bin", "python3")
    
    if osPathExists(local_python):
        resolved_python = local_python
    else:
        parent_venv = osPathJoin(vault_root, ".venv")
        parent_python = osPathJoin(parent_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(parent_venv, "bin", "python3")
        resolved_python = parent_python
        
    if resolved_python and osPathExists(resolved_python):
        print(f"🗑️  Resetting RAG database via {resolved_python} {indexer_script} --reset...")
        subprocessRun([resolved_python, indexer_script, "--reset"])
    else:
        print("❌ Error: Python executable not found for RAG Engine.")

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
        protect_core_kms()

        # 2. Mode Management
        has_rag = check_rag_attached()
        while True:
            print("\n--- 🕹️ Bastien-Antigravity: Mode Selector ---")
            for key, (name, desc) in MODES.items():
                print(f"[{key}] {name.ljust(18)} : {desc}")
            if has_rag:
                print(f"[r] {'🗑️  Reset RAG'.ljust(18)} : Reset and rebuild ChromaDB RAG index.")
            
            choice = input("\nSelect new active mode [1-4] or action (Enter to skip): ").strip().lower()
            if choice == 'r' and has_rag:
                reset_rag_index()
                continue
            break

        if choice in MODES:
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
        
        # Parse active_cli dynamically from MODE-MANUAL.md
        mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
        if osPathExists(mode_file):
            try:
                with open(mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip().startswith("active_cli:"):
                            candidate = line.split(":")[1].strip().lower().replace("'", "").replace('"', '')
                            if candidate in clis:
                                active_cli = candidate
                                break
            except Exception:
                pass
                
        # Support ACTIVE_CLI environment variable override
        env_override = os.getenv("ACTIVE_CLI", "").lower().strip()
        if env_override in clis:
            active_cli = env_override
        
        # Spawn RAG Watcher in the background (Optional: only if 08-RAG-Engine and script exist)
        watcher_script = osPathJoin(script_dir, "../08-RAG-Engine/src/watcher.py")
        watcher_process = None
        
        if osPathExists(watcher_script):
            # Dynamic virtual environment selection: Use local RAG .venv if exist, otherwise fallback to parent .venv
            local_rag_venv = osPathJoin(script_dir, "../08-RAG-Engine", ".venv", "Scripts", "python.exe") if osName == "nt" else osPathJoin(script_dir, "../08-RAG-Engine", ".venv", "bin", "python3")
            parent_venv = osPathJoin(script_dir, "..", ".venv")
            parent_python = osPathJoin(parent_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(parent_venv, "bin", "python3")
            
            if osPathExists(local_rag_venv):
                watcher_venv_python = local_rag_venv
            elif osPathExists(parent_python):
                watcher_venv_python = parent_python
            else:
                watcher_venv_python = None
                
            if watcher_venv_python and osPathExists(watcher_venv_python):
                print(f"📡 Spawning RAG Index Watcher Daemon (Python: {watcher_venv_python}) in the background...")
                try:
                    import subprocess
                    watcher_process = subprocess.Popen(
                        [watcher_venv_python, watcher_script],
                        cwd=osPathDirname(watcher_script),
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                    print("✅ RAG Index Watcher spawned successfully!")
                except Exception as e:
                    print(f"⚠️ Warning: Could not spawn RAG Index Watcher: {e}")
        
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
            if watcher_process:
                watcher_process.terminate()
            break
            
        # 6. Lifecycle Decision
        print("\n--- 🏁 Session Paused ---")
        
        # Terminate background watcher before exiting or restarting
        if watcher_process:
            print("🛑 Terminating background RAG Index Watcher...")
            try:
                watcher_process.terminate()
                watcher_process.wait(timeout=2)
            except Exception:
                try:
                    watcher_process.kill()
                except Exception:
                    pass
            print("✅ RAG Index Watcher terminated.")
            
        has_rag = check_rag_attached()
        prompt_suffix = " / r: Reset RAG" if has_rag else ""
        decision = input(f"Re-launch Squad? [y: Yes / n: Exit & Sign-off / s: Switch Mode{prompt_suffix}]: ").lower().strip()
        
        if decision == 'r' and has_rag:
            reset_rag_index()
            continue
        elif decision == 's' or decision == 'y':
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
    import argparse
    parser = argparse.ArgumentParser(description="Bastien-Antigravity AI Squad Command Center")
    parser.add_argument("--reset-rag", action="store_true", help="Reset and rebuild the ChromaDB RAG index before starting.")
    args, unknown = parser.parse_known_args()

    if args.reset_rag:
        if check_rag_attached():
            reset_rag_index()
        else:
            print("⚠️ Warning: --reset-rag was ignored because 08-RAG-Engine is not attached.")

    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
        sysExit(0)

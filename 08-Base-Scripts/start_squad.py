#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
Initializes the Bastien-Antigravity AI Squad Command Center. Handles MCP binding,
pre-session audits, role synchronization, and launches the selected AI client.

DATA FLOW:
1. Performs Preflight and Sovereignty audits to detect architecture drift.
2. Synchronizes Role-Prompts to agent definitions (convert_agents.py).
3. Invokes the Mode Selector and applies the protocol (switch_mode.py).
4. Configures the MCP server-filesystem based on mode isolation rules.
5. Launches the selected AI client in a re-launchable lifecycle loop.

KEY PARAMETERS:
- vault_root: Resolved path to the Obsidian Brain vault.
- mcp_args: Dynamic arguments for the filesystem MCP server.
"""

from os import makedirs as osMakedirs, listdir as osListdir, name as osName, getenv as osGetenv, remove as osRemove, \
               environ as osEnviron, chmod as osChmod, walk as osWalk
from json import dump as jsonDump, load as jsonLoad
from subprocess import run as subprocessRun
from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists, \
                    expanduser as osPathExpanduser, isdir as osPathIsdir, basename as osPathBasename, getmtime as osPathGetmtime
from sys import exit as sysExit, executable as sysExecutable, path as sysPath, stdout as sysStdout, exit as sysExit

# Add current directory to sys.path to enable library imports
script_dir = osPathDirname(osPathAbspath(__file__))
vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
if script_dir not in sysPath:
    sysPath.append(script_dir)
if vault_root not in sysPath:
    sysPath.append(vault_root)

_venv_python = osPathJoin(vault_root, ".venv", "Scripts", "python.exe") if osName == "nt" else osPathJoin(vault_root, ".venv", "bin", "python3")


try:
    from switch_mode import apply_mode_protocol, MODES
    from mission_help import MissionHelper
    from clients.registry import (
        DEFAULT_CLIENT,
        build_launch_command,
        client_names,
        get_client_config,
        is_client_available,
        list_agents,
        normalize_client,
    )
except ImportError:
    print("❌ Error: Could not find required launcher modules in 08-Base-Scripts/")
    sysExit(1)

# -----------------------------------------------------------------------------------------------

def get_vault_python() -> str:
    """Return the vault virtualenv Python when available, otherwise current Python."""
    return _venv_python if osPathExists(_venv_python) else sysExecutable

# -----------------------------------------------------------------------------------------------

def print_process_manifest_summary() -> None:
    """
    Reads process-manifest.json and prints a beautiful status table of all active components.
    """
    C_RESET = "\033[0m"
    C_GREEN = "\033[92m"
    C_RED = "\033[91m"
    C_BOLD = "\033[1m"

    manifest_path = osPathJoin(vault_root, "00-AI-Orchestration", "process-manifest.json")
    if not osPathExists(manifest_path):
        print(f"{C_RED}⚠️ Process manifest not found at {manifest_path}{C_RESET}")
        return

    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = jsonLoad(f)
    except Exception as e:
        print(f"{C_RED}⚠️ Error loading process manifest: {e}{C_RESET}")
        return

    print("\n" + "═"*75)
    print(f"📊 {C_BOLD}BASTIEN-ANTIGRAVITY: MULTIDIMENSIONAL PROCESS REGISTRY SUMMARY{C_RESET}")
    print("═"*75)
    
    header_format = "{:<20} {:<10} {:<32} {:<10}"
    print(C_BOLD + header_format.format("Component Name", "Type", "Trigger Condition", "Status") + C_RESET)
    print("─"*75)

    all_ok = True
    for category in ["processes", "agents", "concepts"]:
        elements = manifest.get(category, [])
        for el in elements:
            name = el.get("name", "Unknown")
            trigger = el.get("trigger_condition", "N/A")
            assoc_file = el.get("associated_file", "")
            
            if len(trigger) > 30:
                trigger = trigger[:27] + "..."
                
            full_path = osPathJoin(vault_root, assoc_file)
            if osPathExists(full_path):
                status_str = f"{C_GREEN}GREEN [OK]{C_RESET}"
            else:
                status_str = f"{C_RED}RED [DRIFT]{C_RESET}"
                all_ok = False
                
            type_label = category[:-1].upper()
            print(header_format.format(name, type_label, trigger, status_str))

    print("═"*75)
    if all_ok:
        print(f"✨ {C_GREEN}SYSTEM COHERENCE: All active control elements are verified.{C_RESET}")
    else:
        print(f"⚠️  {C_RED}SYSTEM ALERT: Component drift detected! Check missing files.{C_RESET}")
    print("═"*75 + "\n")

# -----------------------------------------------------------------------------------------------

def archive_strat_files() -> None:
    """
    DATA FLOW:
    Finds all STRAT-*.md files in the root of 01-Strategic-Nexus and moves them to 01-Strategic-Nexus/archive/.
    Creates the archive folder if it doesn't exist.
    Updates the links in all Strategy-Nexus markdown files to reflect the new location if needed.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    nexus_dir = osPathJoin(vault_root, "01-Strategic-Nexus")
    if not osPathExists(nexus_dir):
        return
        
    archive_dir = osPathJoin(nexus_dir, "archive")
    
    moved_any = False
    
    try:
        # Scan for STRAT-*.md files in the root of 01-Strategic-Nexus
        for item in osListdir(nexus_dir):
            if item.startswith("STRAT-") and item.endswith(".md"):
                # Create archive folder on demand
                if not osPathExists(archive_dir):
                    try:
                        osMakedirs(archive_dir, exist_ok=True)
                        print("📁 Created archive directory in 01-Strategic-Nexus")
                    except Exception as e:
                        print(f"⚠️ Warning: Could not create archive directory via python: {e}")
                
                src_path = osPathJoin(nexus_dir, item)
                dst_path = osPathJoin(archive_dir, item)
                
                # Robust move with copy+delete fallback to bypass OS permission/metadata locks
                import shutil
                try:
                    shutil.move(src_path, dst_path)
                    print(f"📦 Archived STRAT audit: {item} -> archive/{item}")
                    moved_any = True
                except Exception as e_move:
                    # Fallback to copy and remove
                    try:
                        with open(src_path, "rb") as f_src:
                            with open(dst_path, "wb") as f_dst:
                                f_dst.write(f_src.read())
                        try:
                            osRemove(src_path)
                        except Exception as e_rm:
                            print(f"⚠️ Warning: Could not remove source file {item}: {e_rm}")
                        print(f"📦 Archived STRAT audit (fallback): {item} -> archive/{item}")
                        moved_any = True
                    except Exception as e_copy:
                        print(f"⚠️ Warning: Could not move {item} to archive: {e_move} (fallback failed: {e_copy})")
                
        # If we moved files, update links in all markdown files in 01-Strategic-Nexus (excluding archive/)
        if moved_any:
            import re
            for file_item in osListdir(nexus_dir):
                if file_item.endswith(".md"):
                    file_path = osPathJoin(nexus_dir, file_item)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        # Use negative lookahead to prevent double-archiving already updated links
                        updated_content = re.sub(
                            r'\[\[(?!archive/)(STRAT-\d+-[^\]]+)\]\]',
                            r'[[archive/\1]]',
                            content
                        )
                        
                        if updated_content != content:
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(updated_content)
                            print(f"📝 Updated links in {file_item} to target the archive folder.")
                    except Exception as e:
                        print(f"⚠️ Warning: Could not update links in {file_item}: {e}")
    except Exception as e:
        print(f"⚠️ Warning: Error archiving STRAT files: {e}")

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
    rag_dir = osPathJoin(vault_root, "09-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "core", "server.py")
    has_rag = osPathExists(rag_dir) and osPathExists(rag_server_script)
    
    obsidian_rag_config = None
    mcp_args = None
    
    if has_rag:
                # Determine the Python virtual environment path dynamically:
        # We now use the unified obsidian-brain environment for everything.
        local_python = osPathJoin(vault_root, ".venv", "Scripts", "python.exe") if osName == "nt" else osPathJoin(vault_root, ".venv", "bin", "python3")
        
        if osPathExists(local_python):
            resolved_python = local_python
            print(f"📡 RAG using unified {osPathBasename(vault_root)} virtual environment: {resolved_python}")
        else:
            resolved_python = sysExecutable
            print(f"📡 RAG using system Python fallback: {resolved_python}")
            
        obsidian_rag_config = {
            "command": resolved_python,
            "args": [rag_server_script],
            "env": {
                "SQUAD_ACTIVE_MODE": str(mode_choice),
                "PYTHONPATH": rag_dir
            }
        }
    else:
        # Fallback to standard basic filesystem MCP server
        # --- Dynamic Context Exclusion Logic (The Firewall) ---
        global_excludes = {
            ".obsidian", ".git", ".gemini", ".claude", ".codex", ".deepseek", ".agents",
            "node_modules", "99-Humans", "quick-overview"
        }
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
    
    # 2. Update MCP configs (AI-Agnostic: Gemini, Claude, and Antigravity)
    configs_to_update = [
        # (filepath, label)
        (osPathJoin(osPathExpanduser("~/.gemini"), "settings.json"), "Gemini Settings"),
        (osPathJoin(osPathExpanduser("~/.gemini/antigravity-cli"), "mcp_config.json"), "Antigravity CLI MCP Config"),
        (osPathJoin(osPathExpanduser("~/.gemini/antigravity-cli"), "settings.json"), "Antigravity CLI Settings"),
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
    
    # Priority paths (07-Core-KMS is the standardized location)
    governance_scripts = ["Preflight-Check.py", "Brain-Health-Audit.py"]
    
    for script_name in governance_scripts:
        standard_path = osPathJoin(script_dir, "../07-Core-KMS/Scripts", script_name)
        legacy_path = osPathJoin(workspace_root, "core-kms-brain", "Scripts", script_name)
        
        target = None
        if osPathExists(standard_path):
            target = standard_path
        elif osPathExists(legacy_path):
            target = legacy_path
            
        if target:
            print(f"📡 Executing Governance Audit: {script_name}...")
            subprocessRun([sysExecutable, target])

def check_session_health(mode_choice: str) -> None:
    """
    Checks if there are uncommitted changes across the entire fleet from a previous session.
    Enforces mode-specific rules for unclosed missions.
    """
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    inventory_path = osPathJoin(vault_root, "05-Fleet-Operation", "00-Repo-Control", "inventory.json")
    
    repos_to_check = []
    
    # 1. Load fleet repositories from inventory
    if osPathExists(inventory_path):
        try:
            with open(inventory_path, 'r', encoding='utf-8') as f:
                data = jsonLoad(f)
                repositories = data.get("repositories", [])
                for repo in repositories:
                    repo_path_rel = repo.get("path")
                    repo_abs_path = osPathAbspath(osPathJoin(workspace_root, repo_path_rel))
                    if osPathExists(repo_abs_path) and osPathExists(osPathJoin(repo_abs_path, ".git")):
                        repos_to_check.append({
                            "name": repo.get("name"),
                            "path": repo_abs_path,
                            "is_vault": (repo.get("name") == "obsidian-brain" or repo_abs_path == vault_root)
                        })
        except Exception as e:
            print(f"⚠️ Warning: Failed to load inventory.json: {e}")
            
    # Fallback to checking vault if inventory is missing or empty
    if not repos_to_check:
        repos_to_check.append({
            "name": "obsidian-brain",
            "path": vault_root,
            "is_vault": True
        })
        
    dirty_repos_info = []
    EXCLUSIONS = [".git", ".obsidian", ".gemini", ".claude", ".codex", ".deepseek", ".agents", "Templates", "MODE-MANUAL.md"]
    
    for repo in repos_to_check:
        repo_name = repo["name"]
        repo_path = repo["path"]
        is_vault = repo["is_vault"]
        
        try:
            try:
                result = subprocessRun(
                    ["git", "status", "--porcelain"], 
                    cwd=repo_path, capture_output=True, text=True, check=True
                )
            except FileNotFoundError:
                print("⚠️ Git executable not found; skipping repo health check.")
                continue
            except Exception as e:
                print(f"⚠️ Git status failed for {repo_name}: {e}")
                continue
            uncommitted = []
            for line in result.stdout.splitlines():
                if not line.strip():
                    continue
                status_path = line[3:].strip()
                # Apply exclusions for the vault
                if is_vault:
                    if status_path.endswith(".md"):
                        if any(x in status_path for x in EXCLUSIONS):
                            continue
                        uncommitted.append(status_path)
                else:
                    # Sibling repos: any uncommitted change matters
                    if not any(x in status_path for x in EXCLUSIONS):
                        uncommitted.append(status_path)
                        
            if uncommitted:
                dirty_repos_info.append((repo_name, len(uncommitted)))
        except Exception:
            pass # Git not found or repo missing
            
    if dirty_repos_info:
        if mode_choice == "3":
            # Mode 3 - Strict Block
            print("\n" + "🛑"*30)
            print("🛑 CRITICAL GOVERNANCE VIOLATION: UNCLOSED MISSION DETECTED")
            print("="*60)
            print("The following repositories have uncommitted changes:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("\nIn Mode 3 (Fleet-Commander), startup is STRICTLY BLOCKED to prevent multi-repository drift.")
            print(f"Please run 'python3 ./{osPathBasename(vault_root)}/08-Base-Scripts/close_mission.py' to verify and sign-off.")
            print("="*60)
            print("🛑"*30 + "\n")
            print("👋 Session should be aborted...")
        
        elif mode_choice == "1":
            # Mode 1 - Big warning with confirmation
            print("\n" + "⚠️"*30)
            print("⚠️  WARNING: UNCLOSED MISSION DETECTED")
            print("="*60)
            print("The following repositories have uncommitted changes:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("\nRunning in Mode 1 (Spec-First) with uncommitted changes can lead to state drift and integrity issues.")
            print(f"It is highly recommended to run 'python3 ./{osPathBasename(vault_root)}/08-Base-Scripts/close_mission.py' first.")
            print("="*60)
            print("⚠️"*30 + "\n")
            
            confirm = input("Ignore and start session anyway? [y/N]: ").lower().strip()
            if confirm != 'y':
                print("👋 Session aborted. Please close the previous mission first.")
                sysExit(0)
                
        elif mode_choice == "2":
            # Mode 2 - Simple warning
            print("\n💡 NOTE: The following repositories have uncommitted changes from a previous session:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("")

def regenerate_agents() -> None:
    """
    DATA FLOW:
    Triggers the multi-AI agent converter to ensure prompts are synchronized.
    """
    convert_script = osPathJoin(script_dir, "convert_agents.py")
    if osPathExists(convert_script):
        print("🔄 Synchronizing AI Squad Roles across adapters...")
        subprocessRun([sysExecutable, convert_script])

def unlock_core_kms() -> None:
    """
    Restores write permissions to 07-Core-KMS to allow audits and updates.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    kms_dir = osPathJoin(vault_root, "07-Core-KMS")
    if not osPathExists(kms_dir):
        return
    print("🔓 Restoring write permissions to 07-Core-KMS for audit phase...")
    for root, dirs, files in osWalk(kms_dir):
        for d in dirs:
            dir_path = osPathJoin(root, d)
            try:
                osChmod(dir_path, 0o755)
            except Exception:
                pass
        for f in files:
            file_path = osPathJoin(root, f)
            try:
                osChmod(file_path, 0o644)
            except Exception:
                pass

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
    for root, dirs, files in osWalk(kms_dir):
        for d in dirs:
            dir_path = osPathJoin(root, d)
            try:
                osChmod(dir_path, 0o555)
            except Exception:
                pass
        for f in files:
            file_path = osPathJoin(root, f)
            try:
                osChmod(file_path, 0o444)
            except Exception:
                pass

def check_rag_attached() -> bool:
    """Returns True if the 09-RAG-Engine and its server.py exist."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "09-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "core", "server.py")
    return osPathExists(rag_dir) and osPathExists(rag_server_script)

def reset_rag_index() -> None:
    """
    DATA FLOW:
    Resolves the RAG virtual environment python executable and runs main.py index --reset.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "09-RAG-Engine")
    rag_main_script = osPathJoin(rag_dir, "main.py")
    
    if not osPathExists(rag_main_script):
        print("❌ Error: 09-RAG-Engine/main.py not found. Cannot reset RAG index.")
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
        print(f"🗑️  Resetting RAG database via {resolved_python} {rag_main_script} index --reset...")
        indexer_env = osEnviron.copy()
        indexer_env["PYTHONPATH"] = rag_dir
        indexer_env["ANONYMIZED_TELEMETRY"] = "False"
        indexer_env["CHROMA_TELEMETRY"] = "False"
        indexer_env["HF_HUB_OFFLINE"] = "1"
        indexer_env["TRANSFORMERS_OFFLINE"] = "1"
        subprocessRun([resolved_python, rag_main_script, "index", "--reset"], env=indexer_env)
    else:
        print("❌ Error: Python executable not found for RAG Engine.")

def get_available_agents(active_cli: str) -> list:
    """Reads available agents from the respective agent directory."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    return list_agents(vault_root, active_cli)

def get_active_client_name() -> str:
    """Resolve the active AI client from MODE-MANUAL.md or environment overrides."""
    clients = client_names()
    active_client = DEFAULT_CLIENT

    mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
    if osPathExists(mode_file):
        try:
            with open(mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith("active_cli:") or line.strip().startswith("active_client:"):
                        candidate = normalize_client(
                            line.split(":", 1)[1].strip().lower().replace("'", "").replace('"', '')
                        )
                        if candidate in clients:
                            active_client = candidate
                            break
        except Exception:
            pass

    for env_name in ("ACTIVE_CLIENT", "ACTIVE_CLI"):
        env_override = normalize_client(osGetenv(env_name, ""))
        if env_override in clients:
            active_client = env_override
            break

    return active_client

def run_client_with_fallback(active_client: str, agent_choice: str, mode_choice: str) -> None:
    """Launch the selected AI client, then fall back to other available clients if needed."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    launch_order = [active_client] + [name for name in client_names() if name != active_client]
    cmd_prefix = [] if osName != 'nt' else ["cmd", "/c"]

    for client_name in launch_order:
        config = get_client_config(client_name)
        if not config:
            continue

        if client_name != active_client and not is_client_available(client_name, vault_root):
            continue

        fallback_agents = get_available_agents(client_name)
        selected_agent = agent_choice if agent_choice and agent_choice in fallback_agents else ""

        try:
            cli_cmd = build_launch_command(
                client_name,
                selected_agent,
                squad_mode=mode_choice,
                vault_root=vault_root,
                python_executable=get_vault_python(),
            )
        except ValueError as e:
            print(f"⚠️ Warning: {e}")
            continue

        if client_name != active_client:
            print(f"⚠️ Warning: {active_client} unavailable. Trying fallback client: {client_name}")

        try:
            subprocessRun(cmd_prefix + cli_cmd)
            return
        except FileNotFoundError:
            print(f"⚠️ Warning: Client command '{cli_cmd[0]}' not found on path.")
            continue

    raise FileNotFoundError(f"No available AI client found. Tried: {', '.join(launch_order)}")

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
        unlock_core_kms()
        archive_strat_files()
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
            print(f"[p] {'🎭 Extract Personas'.ljust(18)} : Extract polyglot codebase context in background.")
            
            choice = input("\nSelect new active mode [1-4] or action (Enter to skip): ").strip().lower()
            if choice == 'r' and has_rag:
                reset_rag_index()
                continue
            elif choice == 'p':
                persona_extractor_script = osPathJoin(script_dir, "persona_extractor.py")
                lock_path = osPathAbspath(osPathJoin(script_dir, "..", "07-Core-KMS", "quick-overview", "ast-patterns", ".persona_running"))
                if osPathExists(lock_path):
                    print("⚠️ Persona Extractor is already running. Please wait.")
                elif osPathExists(persona_extractor_script):
                    try:
                        from subprocess import Popen as subProcessPopen, DEVNULL as subProcessDEVNULL
                        subProcessPopen(
                            [sysExecutable, persona_extractor_script, "--daemon"],
                            stdout=subProcessDEVNULL,
                            stderr=subProcessDEVNULL
                        )
                        print("✅ Persona Extractor started in background. It will notify when ready.")
                    except Exception as e:
                        print(f"⚠️ Warning: Could not spawn Persona Extractor: {e}")
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
        check_session_health(choice)
        setup_mcp(choice)
        
        # 4. Display Mission Guidance
        helper = MissionHelper()
        helper.print_cheat_sheet()
        
        # 5. AI Client Execution
        active_cli = get_active_client_name()
        active_config = get_client_config(active_cli) or {}
        active_label = active_config.get("label", active_cli)
        
        # Select Agent Persona dynamically
        available_agents = get_available_agents(active_cli)
        env_agent = osGetenv("ACTIVE_AGENT", "").strip().lower()
        
        if env_agent and env_agent in available_agents:
            agent_choice = env_agent
            print(f"\n🎭 Routing via pre-selected Agent: {agent_choice}")
        elif "orchestrator" in available_agents:
            agent_choice = "orchestrator"
            print(f"\n🎭 Mode {choice} active: Routing via Orchestrator (Universal Gateway).")
        elif available_agents:
            print("\n🎭 Orchestrator persona not found. Available Agent Personas:")
            for idx, agent in enumerate(sorted(available_agents), 1):
                print(f"[{idx}] {agent}")
            print("[0] Generic (Default Session)")
            
            try:
                agent_input = input(f"\nSelect Agent Persona [0-{len(available_agents)}] (Enter for Default): ").strip()
                if agent_input.isdigit():
                    val = int(agent_input)
                    if 1 <= val <= len(available_agents):
                        agent_choice = sorted(available_agents)[val - 1]
            except (KeyboardInterrupt, EOFError):
                pass
        
        print_process_manifest_summary()
        
        if agent_choice:
            print(f"\n🚀 Firing up {active_label} [Protocol: {choice} | Agent: {agent_choice}]...")
        else:
            print(f"\n🚀 Firing up {active_label} [Protocol: {choice} | Agent: Generic]...")
            
        try:
            run_client_with_fallback(active_cli, agent_choice, choice)
        except FileNotFoundError:
            print("❌ No supported AI client is available. Install Gemini, Claude, Codex, or configure DeepSeek.")
        except Exception as e:
            print(f"❌ CLI Execution Error: {e}")
            break
            
        # Check if Persona Extraction is ready
        persona_flag_path = osPathAbspath(osPathJoin(script_dir, "..", "07-Core-KMS", "quick-overview", "ast-patterns", ".persona_ready"))
        if osPathExists(persona_flag_path):
            print("\n" + "✨" * 30)
            print("🚀 NEW PERSONA CONTEXT EXTRACTED AND READY FOR RAG !!")
            print("✨" * 30 + "\a")
            try:
                from os import remove as osRemove
                osRemove(persona_flag_path)
            except Exception:
                pass

        # 6. Lifecycle Decision
        print("\n--- 🏁 Session Paused ---")
        
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
            cancelled_exit = False
            if osPathExists(signoff_script):
                while True:
                    try:
                        result = subprocessRun([sysExecutable, signoff_script], check=True)
                    except FileNotFoundError:
                        print("⚠️ Sign‑off script not found.")
                        break
                    except Exception as e:
                        print(f"⚠️ Sign‑off execution error: {e}")
                        break
                    if result.returncode != 0:
                        print("\n🛑 MISSION SIGN-OFF BLOCKED DUE TO GOVERNANCE VIOLATIONS.")
                        print("Options:")
                        print("  [r] Retry: Run sign-off again.")
                        print("  [i] Force ignore: Exit anyway, bypassing violations.")
                        print("  [c] Cancel exit: Return to the main command loop menu.")
                        user_choice = input("Choice: ").strip().lower()
                        if user_choice == 'r':
                            continue
                        elif user_choice == 'i':
                            print("⚠️ Bypassing governance violations. Exiting.")
                            break
                        elif user_choice == 'c':
                            print("Returning to main menu.")
                            cancelled_exit = True
                            break
                        else:
                            print("Invalid option. Retrying sign-off by default.")
                            continue
                    else:
                        break

            if cancelled_exit:
                continue
            print("👋 Squad resting. Mission concluded.")
            break

# -----------------------------------------------------------------------------------------------

def get_settings_paths() -> list:
    paths = [
        osPathJoin(osPathExpanduser("~/.gemini"), "settings.json"),
        osPathJoin(osPathExpanduser("~/.gemini/antigravity-cli"), "mcp_config.json"),
        osPathJoin(osPathExpanduser("~/.gemini/antigravity-cli"), "settings.json")
    ]
    if osName != "nt":
        paths.append(osPathJoin(osPathExpanduser("~/Library/Application Support/Claude"), "claude_desktop_config.json"))
    else:
        paths.append(osPathJoin(osPathExpanduser("~/AppData/Roaming/Claude"), "claude_desktop_config.json"))
    return paths

def backup_settings() -> None:
    for path in get_settings_paths():
        if osPathExists(path):
            bak_path = path + ".bak"
            if not osPathExists(bak_path):
                try:
                    import shutil
                    shutil.copy2(path, bak_path)
                    print(f"📦 Created backup of {osPathBasename(path)}")
                except Exception as e:
                    print(f"⚠️ Warning: Could not backup {path}: {e}")
            else:
                # Backup already exists; skip to avoid overwriting
                print(f"⚠️ Backup already exists for {osPathBasename(path)}; skipping.")

def restore_settings() -> None:
    for path in get_settings_paths():
        bak_path = path + ".bak"
        if osPathExists(bak_path):
            # Only restore if the original file has not changed since backup
            try:
                original_mtime = osPathGetmtime(path) if osPathExists(path) else None
                backup_mtime = osPathGetmtime(bak_path)
                if original_mtime is None or backup_mtime > original_mtime:
                    import shutil
                    shutil.move(bak_path, path)
                    print(f"📦 Restored original {osPathBasename(path)} from backup")
                else:
                    print(f"⚠️ Original {osPathBasename(path)} unchanged; keeping current version.")
            except Exception as e:
                print(f"⚠️ Warning: Could not restore {path}: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bastien-Antigravity AI Squad Command Center")
    parser.add_argument("--reset-rag", action="store_true", help="Reset and rebuild the ChromaDB RAG index before starting.")
    parser.add_argument("--client", "-c", type=str, help="Specify the active client on startup (e.g. gemini, claude, deepseek, codex, antigravity).")
    parser.add_argument("--agent", "-a", type=str, help="Specify the active agent persona on startup (e.g. oracle, developer, qa).")
    args, unknown = parser.parse_known_args()

    if args.client:
        osEnviron["ACTIVE_CLIENT"] = args.client

    if args.agent:
        osEnviron["ACTIVE_AGENT"] = args.agent

    if args.reset_rag:
        if check_rag_attached():
            reset_rag_index()
        else:
            print("⚠️ Warning: --reset-rag was ignored because 09-RAG-Engine is not attached.")

    backup_settings()
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
    finally:
        restore_settings()
        sysExit(0)

#!/usr/bin/env python
# coding:utf-8
"""
🛡️ SOVEREIGNTY ENGINE (Core Library)
Centralized validation logic for the Bastien-Antigravity Obsidian Brain.
Enforces DocMaintainer and Sentinel rules with high reliability.
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


import re
from pathlib import Path
from typing import Dict, Set

class Sovereignty:
    # --- Configuration ---
    REQUIRED_YAML = ["microservice", "type", "status"]
    MANDATORY_TAG_ROOTS = ["#type/", "#state/"]
    TRANSVERSAL_TAG_ROOTS = ["#tech/", "#tier/", "#zone/"]
    
    # --- Result Structure ---
    def __init__(self, taxonomy_path: Path = None, workspace_root: Path = None):
        self.errors = []
        self.warnings = []
        self.valid_tags = set()
        self.valid_stems = set()
        self.valid_paths = set()
        
        # Determine workspace root (defaults to obsidian-brain)
        if workspace_root is None:
            self.workspace_root = Path(__file__).resolve().parents[2]
        else:
            self.workspace_root = workspace_root
            
        self._index_workspace()
        
        if taxonomy_path and taxonomy_path.exists():
            self._load_taxonomy(taxonomy_path)

    def _index_workspace(self):
        import os
        for root, dirs, files in os.walk(self.workspace_root):
            if any(x in root for x in [".git", ".obsidian", "experiments", "node_modules", "Templates"]):
                continue
            for file in files:
                if file.endswith(".md"):
                    path = Path(root) / file
                    self.valid_stems.add(path.stem)
                    self.valid_paths.add(file)
                    try:
                        rel_path = path.relative_to(self.workspace_root).as_posix()
                        self.valid_paths.add(rel_path)
                    except ValueError:
                        pass

    def _load_taxonomy(self, path: Path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Find all #tag/ or #tag patterns
                found = re.findall(r'#[\w/-]+', content)
                for t in found:
                    self.valid_tags.add(t)
        except Exception as e:
            self.log_warning(f"Could not load taxonomy from {path}: {e}")

    def log_error(self, message: str):
        self.errors.append(message)

    def log_warning(self, message: str):
        self.warnings.append(message)

    # --- Validation Methods ---

    def validate_frontmatter(self, content: str, file_name: str) -> bool:
        """Checks for mandatory YAML frontmatter fields."""
        if not content.startswith("---"):
            self.log_error(f"[{file_name}] Missing YAML frontmatter.")
            return False

        parts = content.split("---", 2)
        if len(parts) < 3:
            self.log_error(f"[{file_name}] Malformed YAML frontmatter.")
            return False

        yaml_block = parts[1]
        missing = [f for f in self.REQUIRED_YAML if f"{f}:" not in yaml_block]
        
        for field in missing:
            self.log_error(f"[{file_name}] Missing mandatory field: '{field}'")
            
        return len(missing) == 0

    def validate_taxonomy(self, content: str, file_name: str):
        """Ensures mandatory and transversal tags are present."""
        # 1. Mandatory Roots
        for tag_root in self.MANDATORY_TAG_ROOTS:
            if tag_root not in content:
                self.log_warning(f"[{file_name}] Missing recommended taxonomy tag: '{tag_root}'")
        
        # 2. Transversal Trinity (Need at least one of these)
        if not any(t in content for t in self.TRANSVERSAL_TAG_ROOTS):
            self.log_error(f"[{file_name}] TRANSVERSAL ERROR: File must have at least one #tech/, #tier/, or #zone/ tag.")

    def validate_isolation_zone(self, repo_path: Path, repo_name: str) -> bool:
        """Checks for the presence and structure of the isolation zone."""
        is_brain = (repo_name == "obsidian-brain")
        zone_name = "99-Humans" if is_brain else "quick-overview"
        zone_dir = repo_path / zone_name
        
        if not zone_dir.exists():
            self.log_error(f"[{repo_name}] Missing mandatory isolation zone: {zone_name}")
            return False
            
        # Define mandatory files for the zone
        if is_brain:
            # Brain only requires the core dashboards
            mandatory = ["Sprint-Dashboard.md", "Domain-Dashboard.md"]
        else:
            # Microservices require the full structural quartet
            mandatory = [
                "Architecture-Overview.md", 
                "Features-Behavior.md", 
                "Testing-Playbook.md", 
                "General-Misc.md"
            ]
            
        success = True
        for filename in mandatory:
            if not (zone_dir / filename).exists():
                self.log_error(f"[{repo_name}] Missing file in {zone_name}: {filename}")
                success = False
        
        return success

    def validate_links(self, content: str, file_name: str):
        """Identifies broken [[Links]]."""
        # Extract [[Link]] or [[Link|Alias]]
        links = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]*)?\]\]', content)
        
        for link in links:
            clean_link = link.strip().replace("\\", "/")
            link_stem = Path(clean_link).stem
            
            # Check against stems, full relative paths, or exact filenames
            if clean_link in self.valid_stems or clean_link in self.valid_paths or link_stem in self.valid_stems:
                continue
                
            # If it's a direct file reference with extension
            if any(clean_link.endswith(ext) for ext in [".md", ".json"]):
                # This would need a full file list to be perfect, 
                # for now we flag it if not in paths
                if clean_link not in self.valid_paths:
                    self.log_error(f"[{file_name}] Broken link: [[{link}]]")
            else:
                # Assume .md if no extension
                if f"{clean_link}.md" not in self.valid_paths:
                    self.log_error(f"[{file_name}] Broken link: [[{link}]]")

    def validate_telemetry(self, content: str, file_name: str):
        """Ensures Roles have the [SCAN] block."""
        # Only enforce on core agent definitions or role prompts
        if any(x in file_name.lower() for x in ["role-", "prompt-", "agent-"]):
            if "[SCAN]" not in content:
                self.log_error(f"[{file_name}] Role definition missing mandatory [SCAN] telemetry block.")

    def validate_utc_mandate(self, content: str, file_name: str):
        """Heuristic check for prohibited local time references."""
        # Very basic check for common local time indicators if they aren't followed by 'UTC' or 'Z'
        # This is a warning-only check as it can have false positives
        local_time_patterns = [
            r'\d{1,2}:\d{2} (AM|PM)(?!.*UTC)',
            r'Local Time',
            r'Heure locale'
        ]
        for pattern in local_time_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.log_warning(f"[{file_name}] Potential 'Local Time' detected. Ensure UTC mandate is followed.")

    def validate_session_state(self, content: str, file_name: str):
        """Checks for Mission-ID in session states."""
        if "AI-Session-State" in file_name:
            if not re.search(r'Mission-ID:|Trace-ID:|X-Bastien-Mission-ID', content, re.IGNORECASE):
                self.log_error(f"[{file_name}] Session state entry missing Mission/Trace ID.")

    def validate_orphan_tags(self, content: str, file_name: str):
        """Identifies tags not defined in the taxonomy, ignoring hex colors."""
        if not self.valid_tags:
            return
            
        tags = re.findall(r'#([\w/-]+)', content)
        for t in tags:
            full_tag = f"#{t}"
            
            # Skip hex colors (3 or 6 hex digits)
            if re.match(r'^[0-9a-fA-F]{3}$|^[0-9a-fA-F]{6}$', t):
                continue
            
            # Check if valid
            is_valid = False
            for v in self.valid_tags:
                if full_tag == v or (v.endswith("/") and full_tag.startswith(v)):
                    is_valid = True
                    break
            
            if not is_valid:
                self.log_warning(f"[{file_name}] Orphan tag detected: {full_tag}")

    # --- Orchestration ---

    def audit_file(self, path: Path):
        """Runs the full suite against a single file."""
        if not path.suffix == ".md":
            return

        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_name = path.name
            
            self.validate_frontmatter(content, file_name)
            self.validate_taxonomy(content, file_name)
            self.validate_orphan_tags(content, file_name)
            self.validate_links(content, file_name)
            self.validate_telemetry(content, file_name)
            self.validate_utc_mandate(content, file_name)
            self.validate_session_state(content, file_name)
            self.validate_placeholders(content, file_name)
            self.validate_hardcoded_paths(content, file_name)
            
        except Exception as e:
            self.log_error(f"Failed to read {path.name}: {str(e)}")

    def validate_placeholders(self, content: str, file_name: str):
        """Ensures that template placeholders like {{microservice}} are resolved."""
        placeholders = re.findall(r'\{\{[\w-]+\}\}', content)
        if placeholders:
            for p in placeholders:
                self.log_error(f"[{file_name}] Unresolved placeholder detected: {p}")

    def validate_hardcoded_paths(self, content: str, file_name: str):
        """Ensures that no hardcoded absolute local paths are used in links."""
        matches = re.findall(r'(\bfile:///Users/[^\s)\]\n\r]+|\b/Users/[^\s)\]\n\r]+|\bfile:///home/[^\s)\]\n\r]+|\b/home/[^\s)\]\n\r]+)', content)
        if matches:
            for m in matches:
                self.log_error(f"[{file_name}] Hardcoded absolute path detected: {m}")

    def auto_fix_file(self, path: Path):
        """Fixes taxonomy issues and automatically converts absolute links to relative ones."""
        if not path.suffix == ".md":
            return
            
        try:
            import yaml
            import os
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    yaml_block = parts[1]
                    try:
                        data = yaml.safe_load(yaml_block) or {}
                        modified = False
                        
                        if not isinstance(data, dict):
                            data = {}
                            
                        # Handle tags
                        tags = data.get('tags', [])
                        if not isinstance(tags, list):
                            tags = [tags] if tags else []
                        
                        new_tags = []
                        for tag in tags:
                            if not tag or str(tag).lower() == 'null':
                                modified = True
                                continue
                            
                            tag_str = str(tag).replace("\\", "").replace("'", "").replace('"', "").strip()
                            if tag_str.startswith('domain/'):
                                new_tags.append('#' + tag_str)
                                modified = True
                            elif tag_str.startswith('/'):
                                new_tags.append('#' + tag_str[1:])
                                modified = True
                            else:
                                new_tags.append(tag_str)
                        
                        # Inject #service tag based on microservice key
                        microservice = data.get('microservice')
                        if microservice and str(microservice).lower() != 'null':
                            service_tag = f"#service/{str(microservice).strip('\"\'')}"
                            if service_tag not in new_tags:
                                new_tags.append(service_tag)
                                modified = True
                                
                        # Inject default transversal tag (#zone/3-fleet) if none are present
                        if not any(t in str(tag) for t in ["#tech/", "#tier/", "#zone/"] for tag in new_tags):
                            new_tags.append("#zone/3-fleet")
                            modified = True
                            
                        if modified or 'tags' not in data:
                            if new_tags:
                                data['tags'] = new_tags
                            else:
                                data['tags'] = []
                                
                            new_yaml_block = yaml.dump(data, default_flow_style=False, sort_keys=False)
                            content = f"---\n{new_yaml_block}---{parts[2]}"
                    except yaml.YAMLError as e:
                        self.log_warning(f"YAML parsing failed for {path.name}: {e}. Falling back to old content.")
            
            # Auto-fix absolute links to dynamic relative links
            absolute_links = re.findall(r'\[([^\]]*)\]\((file:///Users/[^\s)\]]+|/Users/[^\s)\]]+|file:///home/[^\s)\]]+|/home/[^\s)\]]+)\)', content)
            for text, target_url in absolute_links:
                clean_path_str = target_url.replace("file://", "")
                target_path = Path(clean_path_str).resolve()
                if target_path.exists():
                    rel_path = os.path.relpath(target_path, path.parent)
                    rel_path_str = Path(rel_path).as_posix()
                    old_link = f"[{text}]({target_url})"
                    new_link = f"[{text}]({rel_path_str})"
                    content = content.replace(old_link, new_link)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            self.log_warning(f"Auto-fix failed for {path.name}: {str(e)}")

    def get_report(self) -> Dict:
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "success": len(self.errors) == 0
        }


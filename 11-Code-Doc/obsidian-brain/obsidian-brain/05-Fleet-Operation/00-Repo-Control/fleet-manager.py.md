---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|DefaultLogger]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|FleetManager]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_detect_language_path]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_do]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_ensure_auth]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_find_workspace_root]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_attach]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_audit]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_branch]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_cleanup]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_commit]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_discover]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_refresh]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_restore]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_tag]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_template]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_handle_vault_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_load_job_fragment]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|_resolve_inventory_paths]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|attach_repo]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|audit_repo]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|cleanup_repo]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|critical]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|discover_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|error]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|get_github_token]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|get_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|info]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|run]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|run_git]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|sync_repo]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|template_repo]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|warning]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|DefaultLogger]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|MInventoryBuilder]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_abort_if_self_on_forbidden_branch]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_assert_not_forbidden_branch]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_build_manual_overrides]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_detect_repo_type]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_discover_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_has_code_at_root]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_is_knowledge_base]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_load_existing_inventory]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|_run_git]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|build]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|critical]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|error]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|info]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|resolve_vault_and_workspace]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|setup_terminal]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/build-inventory.py.md|warning]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|fleet-manager.py]] (calls)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/00-Repo-Control/fleet-manager.py.md|fleet-manager.py]] (same_package)
<!-- SYNC:END -->

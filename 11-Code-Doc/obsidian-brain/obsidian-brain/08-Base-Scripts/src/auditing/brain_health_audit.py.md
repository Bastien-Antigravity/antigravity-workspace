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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/auditor.py.md|Auditor]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|audit_file]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|auto_fix_file]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|BrainSentinel]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|IGNORE_DIRS]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|audit]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|auto_fix]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|report]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|scan]] (function: belongs_to)
<!-- SYNC:END -->
 belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|scan]] (function: belongs_to)
<!-- SYNC:END -->

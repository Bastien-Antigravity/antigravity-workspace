

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/check_coherence.py.md|check_coherence.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|ZONE_MAP]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|_find_workspace_root]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|apply_hardening]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (same_package)
<!-- SYNC:END -->

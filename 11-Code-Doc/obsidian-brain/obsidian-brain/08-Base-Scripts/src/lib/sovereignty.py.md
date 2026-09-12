

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|add]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/close_mission.py.md|close_mission.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|Sovereignty]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|_index_workspace]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|_load_taxonomy]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|audit_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|auto_fix_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|get_report]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|is_ignored_by_firewall]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|log_error]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|log_warning]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_frontmatter]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_hardcoded_paths]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_isolation_zone]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_links]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_orphan_tags]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_placeholders]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_session_state]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_taxonomy]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_telemetry]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_utc_mandate]] (function: belongs_to)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|audit_file]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_isolation_zone]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|FleetCommander]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_load_inventory]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_log]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_resolve_active_workspaces]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_run_command]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_step]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|audit_docs]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|audit_isolation_zone]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|execute_fleet_push]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|validate_architecture]] (function: belongs_to)
<!-- SYNC:END -->

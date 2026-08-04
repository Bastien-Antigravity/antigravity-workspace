

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_init_update.py.md|INVENTORY_PATH]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_init_update.py.md|TEMPLATE]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_init_update.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_init_update.py.md|update_fleet]] (function: belongs_to)
<!-- SYNC:END -->

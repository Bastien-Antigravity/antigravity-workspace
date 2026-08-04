

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|PostgresMemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|set_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|resolve_schema_name]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
<!-- SYNC:END -->

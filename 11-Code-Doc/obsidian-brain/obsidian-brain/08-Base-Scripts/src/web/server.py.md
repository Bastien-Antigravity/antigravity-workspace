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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|register_routes]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|rest_handler.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|init_routes]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|register_mfe_with_web_interface]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|start_async_server]] (function: belongs_to)
<!-- SYNC:END -->

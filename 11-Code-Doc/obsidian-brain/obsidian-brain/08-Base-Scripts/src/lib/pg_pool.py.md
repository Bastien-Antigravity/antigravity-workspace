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
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|close_pg_pool]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|get_pg_pool]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|resolve_schema_name]] (function: belongs_to)
<!-- SYNC:END -->

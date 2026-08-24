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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|add]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|memory_store.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|EventDeduplicator]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|LocalEventBus]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|SquadEventBus]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|_get_subscribers]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|close]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|connect]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|is_duplicate]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|nats_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|publish]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to)
<!-- SYNC:END -->

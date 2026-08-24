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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|Watcher]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_debounced_runner]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_event]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_created]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_modified]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|start]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|stop]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|UniLog]] (class: calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|close]] (function: calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|get_config]] (function: calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|set_config]] (function: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/test_memory_leak.py.md|get_memory_usage]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_memory_leak.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

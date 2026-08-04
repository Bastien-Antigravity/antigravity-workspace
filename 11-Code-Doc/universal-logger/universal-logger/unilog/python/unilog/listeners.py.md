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
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|ConfigUpdateListener]] (class: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__aiter__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__anext__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__del__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__init__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|_put]] (function: belongs_to)
<!-- SYNC:END -->

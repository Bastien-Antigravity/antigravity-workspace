---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
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
- [[universal-logger/universal-logger/unilog/python/unilog/lib_loader.py.md|lib_loader.py]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|get_memory_usage]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|main]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|run_leak_test]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|test_leak_comparison]] (function: belongs_to)
<!-- SYNC:END -->

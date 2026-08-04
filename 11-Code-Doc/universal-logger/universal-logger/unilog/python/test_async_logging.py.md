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
- [[universal-logger/universal-logger/unilog/python/setup.py.md|run]] (function: calls)
- [[universal-logger/universal-logger/unilog/python/setup.py.md|setup.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/__init__.py.md|__init__.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_debug]] (function: calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_info]] (function: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|TestAsyncLogging]] (class: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|heartbeat]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|run_test]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|test_async_caller_metadata]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|test_loop_responsiveness]] (function: belongs_to)
<!-- SYNC:END -->

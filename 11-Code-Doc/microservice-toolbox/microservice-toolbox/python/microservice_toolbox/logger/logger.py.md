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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|facade.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|facade.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|facade.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|Logger]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|PythonLogger]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|add_metadata]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|critical]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|debug]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|ensure_safe_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|error]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|info]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|logon]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|logout]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|report]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|schedule]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|stream]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|trade]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|warning]] (function: belongs_to)
<!-- SYNC:END -->

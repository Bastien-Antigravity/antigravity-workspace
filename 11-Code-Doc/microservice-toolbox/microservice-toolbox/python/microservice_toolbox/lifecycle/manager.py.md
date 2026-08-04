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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|LifecycleManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|_execute_cleanups]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|new_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|new_manager_with_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|register]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|signal_handler]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|wait]] (function: belongs_to)
<!-- SYNC:END -->
o)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/lifecycle/manager.py.md|wait]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|get_hostname]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|helpers.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|helpers.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|process_lock.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|process_lock.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|print_internal_log]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|truncate]] (function: belongs_to)
<!-- SYNC:END -->

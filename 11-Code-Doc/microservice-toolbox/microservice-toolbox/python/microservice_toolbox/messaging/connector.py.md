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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/config.py.md|config.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/connector.py.md|closed_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/connector.py.md|connect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/connector.py.md|disconnected_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/messaging/connector.py.md|reconnected_cb]] (function: belongs_to)
<!-- SYNC:END -->

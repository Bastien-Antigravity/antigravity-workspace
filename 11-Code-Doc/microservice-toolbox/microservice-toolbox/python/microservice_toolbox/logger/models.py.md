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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|LogLevel]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|from_str]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (calls)
<!-- SYNC:END -->

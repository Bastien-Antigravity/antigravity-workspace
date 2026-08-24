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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|new_resolver]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolve_full_bind_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolver.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|GRPCServer]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|start]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|stop]] (function: belongs_to)
<!-- SYNC:END -->

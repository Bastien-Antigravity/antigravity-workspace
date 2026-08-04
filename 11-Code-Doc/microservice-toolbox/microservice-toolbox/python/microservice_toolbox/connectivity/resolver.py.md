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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|Resolver]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|get_primary_interface_ip]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|is_loopback]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|new_resolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolve_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolve_full_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|grpc_server.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|grpc_server.py]] (imports)
<!-- SYNC:END -->

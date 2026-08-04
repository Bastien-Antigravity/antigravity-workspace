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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|providers.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|providers.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|providers.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|ISerializer]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|T]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|marshal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|unmarshal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|providers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (calls)
<!-- SYNC:END -->

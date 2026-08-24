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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|ISerializer]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|T]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|serializer.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|serializer.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|BinSerializer]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|JSONSerializer]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|marshal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|new_bin_serializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|new_json_serializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|unmarshal]] (function: belongs_to)
<!-- SYNC:END -->

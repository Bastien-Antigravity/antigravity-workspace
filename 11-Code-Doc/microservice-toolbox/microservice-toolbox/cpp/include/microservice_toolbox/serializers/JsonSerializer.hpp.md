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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer.Marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer.Unmarshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/Serializer.hpp.md|Serializer.hpp]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer.Marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer.Unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|JsonSerializer]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/serializers/JsonSerializer.hpp.md|MICROSERVICE_TOOLBOX_SERIALIZERS_JSON_SERIALIZER_HPP]] (macro: belongs_to)
<!-- SYNC:END -->

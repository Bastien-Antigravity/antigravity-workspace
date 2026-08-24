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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Serialize]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|T]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.unmarshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.unmarshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.new_bin]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.new_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.unmarshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|Serializer]] (trait: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer.unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|BinSerializer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer.unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|JsonSerializer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.new_bin]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.new_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum.unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|SerializerEnum]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|TestData]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|new_bin_serializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|new_json_serializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|test_serializers_roundtrip]] (function: belongs_to)
<!-- SYNC:END -->

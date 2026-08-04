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
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Marshal]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Unmarshal]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewBinSerializer]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewJSONSerializer]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|providers.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|TestData]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|TestSerializers_Errors]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|TestSerializers_RoundTrip]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_con.go.md|matrix_con.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_gen.go.md|matrix_gen.go]] (imports)
<!-- SYNC:END -->

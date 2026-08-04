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
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewBinSerializer]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewJSONSerializer]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|serializer_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_con.go.md|IntegrationData]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_con.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

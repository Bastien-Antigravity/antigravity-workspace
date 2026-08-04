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
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Deserialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Serialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|SystemTimestamp]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|WrapMarketEvent]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|models_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|models_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|providers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (calls)
<!-- SYNC:END -->

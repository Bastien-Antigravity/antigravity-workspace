---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Deserialize]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Serialize]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|WrapMarketEvent]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|helpers.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestMarketEventSerialization]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestOHLCVSerialization]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestSignalSerialization]] (function: belongs_to)
<!-- SYNC:END -->

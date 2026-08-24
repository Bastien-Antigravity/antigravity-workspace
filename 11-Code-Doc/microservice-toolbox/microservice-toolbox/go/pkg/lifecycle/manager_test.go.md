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
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Register]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Wait]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|NewManager]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager_test.go.md|TestManager_Lifecycle]] (function: belongs_to)
<!-- SYNC:END -->
)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager_test.go.md|TestManager_Lifecycle]] (function: belongs_to)
<!-- SYNC:END -->

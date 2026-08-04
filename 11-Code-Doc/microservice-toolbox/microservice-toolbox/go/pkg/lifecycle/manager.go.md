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
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Register]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Wait]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Register]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Wait]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|NewManagerWithLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|NewManager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|ShutdownFunc]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager_test.go.md|manager_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager_test.go.md|manager_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|manager.rs]] (calls)
<!-- SYNC:END -->

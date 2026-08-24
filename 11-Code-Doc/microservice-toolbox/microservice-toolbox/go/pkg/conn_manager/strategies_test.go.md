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
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.Connect]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewCriticalStrategy]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewPerformanceStrategy]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewStandardStrategy]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|TestStrategies]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|TestUnifiedConnect]] (function: belongs_to)
<!-- SYNC:END -->

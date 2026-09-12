

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectNonBlocking]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectWithRetry]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestConnectNonBlocking]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestOnErrorUnifiedHook]] (function: belongs_to)
<!-- SYNC:END -->

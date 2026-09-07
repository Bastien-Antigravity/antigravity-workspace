

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/core/request_handler.go.md|ProcessRequest]] (function: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/connection.go.md|Server.handleConnection]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/server/connection.go.md|Server.handleConnection]] (method: belongs_to)
- [[config-server/config-server/src/server/connection.go.md|Server]] (struct: defines_method)
- [[config-server/config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)
<!-- SYNC:END -->

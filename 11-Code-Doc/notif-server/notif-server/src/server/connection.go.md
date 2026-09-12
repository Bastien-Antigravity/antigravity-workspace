

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/server/connection.go.md|Server.handleConnection]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/server/connection.go.md|Server.handleConnection]] (method: belongs_to)
- [[notif-server/notif-server/src/server/connection.go.md|Server]] (struct: defines_method)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (same_package)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/notif_server_grpc.pb.go.md|RegisterNotifControlServiceServer]] (function: calls)
- [[notif-server/notif-server/src/grpc_control/service.go.md|NewControlService]] (function: calls)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|RegisterNotifServiceServer]] (function: calls)
- [[notif-server/notif-server/src/server/connection.go.md|Server.handleConnection]] (method: calls)
- [[notif-server/notif-server/src/server/connection.go.md|connection.go]] (same_package)
- [[notif-server/notif-server/src/server/server.go.md|Server.Start]] (method: defines_method)
- [[notif-server/notif-server/src/server/server.go.md|Server.Stop]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: belongs_to)
- [[notif-server/notif-server/src/server/server.go.md|Server.Start]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server.go.md|Server.Stop]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server.go.md|Server]] (struct: belongs_to)
- [[notif-server/notif-server/src/server/server.go.md|Server]] (struct: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (same_package)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (calls)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (same_package)
<!-- SYNC:END -->

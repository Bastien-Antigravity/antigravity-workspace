

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/grpc_control/config_server.pb.go.md|ControlResponse.String]] (method: calls)
- [[config-server/config-server/src/grpc_control/config_server.pb.go.md|config_server.pb.go]] (same_package)
- [[config-server/config-server/src/grpc_control/config_server_grpc.pb.go.md|RegisterConfigControlServiceServer]] (function: calls)
- [[config-server/config-server/src/grpc_control/config_server_grpc.pb.go.md|config_server_grpc.pb.go]] (same_package)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.IsRunning]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.Start]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.Stop]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|NewControlService]] (function: calls)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (same_package)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.IsRunning]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.Start]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService.Stop]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService]] (struct: belongs_to)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|GRPCService]] (struct: defines_method)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|NewGRPCService]] (function: belongs_to)
<!-- SYNC:END -->

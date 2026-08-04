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
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.IsRunning]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.Start]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.Stop]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/notif_server.pb.go.md|ControlResponse.String]] (method: calls)
- [[notif-server/notif-server/src/grpc_control/notif_server.pb.go.md|notif_server.pb.go]] (same_package)
- [[notif-server/notif-server/src/grpc_control/notif_server_grpc.pb.go.md|RegisterNotifControlServiceServer]] (function: calls)
- [[notif-server/notif-server/src/grpc_control/notif_server_grpc.pb.go.md|notif_server_grpc.pb.go]] (same_package)
- [[notif-server/notif-server/src/grpc_control/service.go.md|NewControlService]] (function: calls)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (same_package)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.IsRunning]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.Start]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService.Stop]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService]] (struct: belongs_to)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|GRPCService]] (struct: defines_method)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|NewGRPCService]] (function: belongs_to)
<!-- SYNC:END -->
truct: defines_method)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|NewGRPCService]] (function: belongs_to)
<!-- SYNC:END -->

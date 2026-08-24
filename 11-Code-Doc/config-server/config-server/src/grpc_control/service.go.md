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
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.GetConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.ListConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.PersistConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.SetConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Debug]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (same_package)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.GetConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.ListConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.PersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl.SetConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: defines_method)
- [[config-server/config-server/src/grpc_control/service.go.md|NewControlService]] (function: belongs_to)
<!-- SYNC:END -->

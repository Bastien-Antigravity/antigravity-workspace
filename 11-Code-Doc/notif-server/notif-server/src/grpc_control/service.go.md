

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.AddProvider]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetSupportedTypes]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ListNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.RemoveProvider]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SendTestNotification]] (method: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SetAlertingConfig]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[notif-server/notif-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (same_package)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.AddProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetSupportedTypes]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ListNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.RemoveProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SendTestNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: belongs_to)
- [[notif-server/notif-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: defines_method)
- [[notif-server/notif-server/src/grpc_control/service.go.md|NewControlService]] (function: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (imports)
<!-- SYNC:END -->
tif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (imports)
<!-- SYNC:END -->

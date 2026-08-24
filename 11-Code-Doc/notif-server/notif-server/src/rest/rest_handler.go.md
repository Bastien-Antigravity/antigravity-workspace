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
- [[notif-server/notif-server/src/core/controller.go.md|Controller.AddProvider]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetAlertingConfig]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetStatus]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetSupportedTypes]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.ListNotifiers]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.ReloadConfig]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.RemoveProvider]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SendTestNotification]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/service.go.md|NewControlService]] (function: calls)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleAddProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetSupportedTypes]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleListNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleRemoveProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSendTest]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleAddProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetSupportedTypes]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleListNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleRemoveProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSendTest]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: defines_method)
<!-- SYNC:END -->

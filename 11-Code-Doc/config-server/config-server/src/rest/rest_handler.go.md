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
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleGetConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleListConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handlePersistConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleSetConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.GetConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.GetStatus]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.ListConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.PersistConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.ReloadConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.SetConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleGetConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleListConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handlePersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleSetConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpControlResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpGetResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpListResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpSetConfigRequest]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpStatusResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
<!-- SYNC:END -->

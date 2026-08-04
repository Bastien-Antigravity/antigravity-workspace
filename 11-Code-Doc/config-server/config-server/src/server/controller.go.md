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
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Debug]] (method: calls)
- [[config-server/config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: defines_method)
- [[config-server/config-server/src/server/controller.go.md|Server.GetConfig]] (method: defines_method)
- [[config-server/config-server/src/server/controller.go.md|Server.GetStatus]] (method: defines_method)
- [[config-server/config-server/src/server/controller.go.md|Server.ListConfig]] (method: defines_method)
- [[config-server/config-server/src/server/controller.go.md|Server.PersistConfig]] (method: defines_method)
- [[config-server/config-server/src/server/controller.go.md|Server.SetConfig]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|DeepCopy]] (function: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)
- [[config-server/config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/cmd/test/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (imports)
- [[config-server/config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server.GetConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server.GetStatus]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server.ListConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server.PersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server.SetConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/controller.go.md|Server]] (struct: defines_method)
<!-- SYNC:END -->

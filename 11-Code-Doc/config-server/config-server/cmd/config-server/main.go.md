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
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|NewGRPCService]] (function: calls)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[config-server/config-server/src/rest/mfe.js.md|mfe.js]] (imports)
- [[config-server/config-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: calls)
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: calls)
- [[config-server/config-server/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

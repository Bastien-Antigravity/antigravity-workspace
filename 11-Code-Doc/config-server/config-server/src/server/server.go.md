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
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/connection.go.md|Server.handleConnection]] (method: calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.ReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.Start]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.Stop]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.persistenceWorker]] (method: defines_method)
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: defines_method)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)
- [[config-server/config-server/src/store/store.go.md|Store]] (struct: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/cmd/test/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.ReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.Start]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.Stop]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.persistenceWorker]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server]] (struct: belongs_to)
- [[config-server/config-server/src/server/server.go.md|Server]] (struct: defines_method)
- [[config-server/config-server/src/server/server.go.md|clientMailbox]] (struct: belongs_to)
<!-- SYNC:END -->

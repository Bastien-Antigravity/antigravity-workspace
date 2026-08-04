---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: calls)
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/test/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

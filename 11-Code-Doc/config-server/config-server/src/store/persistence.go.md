

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: defines_method)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/cmd/test/main.go.md|main.go]] (calls)
- [[config-server/config-server/cmd/test/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (imports)
- [[config-server/config-server/src/helpers/config_updates.go.md|config_updates.go]] (imports)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (imports)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (imports)
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: belongs_to)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager]] (struct: belongs_to)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager]] (struct: defines_method)
- [[config-server/config-server/src/store/persistence_test.go.md|persistence_test.go]] (calls)
- [[config-server/config-server/src/store/persistence_test.go.md|persistence_test.go]] (same_package)
<!-- SYNC:END -->

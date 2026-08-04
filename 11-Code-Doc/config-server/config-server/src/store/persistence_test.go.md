

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (same_package)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Error]] (method: defines_method)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Info]] (method: defines_method)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/store/persistence_test.go.md|TestPersistenceLoadNonExistent]] (function: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|TestPersistenceSaveLoad]] (function: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger]] (struct: belongs_to)
- [[config-server/config-server/src/store/persistence_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

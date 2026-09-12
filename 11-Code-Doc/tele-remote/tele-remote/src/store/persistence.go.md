

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Load]] (method: defines_method)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Save]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/store/persistence.go.md|NewPersistenceManager]] (function: belongs_to)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Load]] (method: belongs_to)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Save]] (method: belongs_to)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager]] (struct: defines_method)
<!-- SYNC:END -->

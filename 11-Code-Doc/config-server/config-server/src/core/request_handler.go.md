

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/helpers/config_updates.go.md|ApplyUpdates]] (function: calls)
- [[config-server/config-server/src/helpers/config_updates.go.md|config_updates.go]] (imports)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)
- [[config-server/config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/core/request_handler.go.md|ProcessRequest]] (function: belongs_to)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (calls)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|DeepCopy]] (function: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (imports)
- [[config-server/config-server/src/helpers/config_updates.go.md|ApplyUpdates]] (function: belongs_to)
<!-- SYNC:END -->

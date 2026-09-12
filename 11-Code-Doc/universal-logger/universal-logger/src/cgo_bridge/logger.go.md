

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetLevel]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_AddMetadata]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_GetLevel]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_LogWithMetadata]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetLevel]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetMetadata]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->

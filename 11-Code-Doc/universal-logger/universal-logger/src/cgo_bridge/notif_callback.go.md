

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|UniLog_RegisterNotifCallback]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|internalNotificationPump]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->

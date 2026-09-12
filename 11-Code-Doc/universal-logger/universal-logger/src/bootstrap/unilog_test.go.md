

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (same_package)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (imports)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|TestInitWithLocalNotifier]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|TestInitWithoutLocalNotifier]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
<!-- SYNC:END -->

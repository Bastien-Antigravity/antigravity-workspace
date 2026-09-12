

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (imports)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.GetConfig]] (method: calls)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: calls)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Critical]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Debug]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: calls)
- [[universal-logger/universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

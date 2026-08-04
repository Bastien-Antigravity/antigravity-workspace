

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: calls)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|NewDistributedConfig]] (function: calls)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|config_handler.go]] (imports)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|NewUniLog]] (function: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLocalNotifQueue]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|logger_handler.go]] (imports)
- [[universal-logger/universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (same_package)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (same_package)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|BootstrapOptions]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitWithOptions]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (calls)
<!-- SYNC:END -->

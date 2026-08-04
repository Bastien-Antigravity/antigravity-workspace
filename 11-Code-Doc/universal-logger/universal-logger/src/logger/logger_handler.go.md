---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Critical]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Debug]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Log]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logon]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logout]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Report]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Schedule]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetCallerSkip]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLocalNotifQueue]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Stream]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Trade]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Unwrap]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (imports)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|logger.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|notif_callback.go]] (calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|NewUniLog]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Critical]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Debug]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Log]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logon]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logout]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Report]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Schedule]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetCallerSkip]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLocalNotifQueue]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Stream]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Trade]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Unwrap]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog]] (struct: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|logger_utils.go]] (calls)
<!-- SYNC:END -->

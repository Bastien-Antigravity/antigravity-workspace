---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Critical]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Debug]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.GetLevel]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Log]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Logon]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Logout]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Report]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Schedule]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.SetCallerSkip]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.SetLevel]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Stream]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Trade]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Warning]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.getEntry]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|MockNotifier.Notify]] (method: calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|MockSink.Write]] (method: calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/flexible-logger/main.go.md|main.go]] (calls)
- [[flexible-logger/flexible-logger/cmd/test-log-server/connection_test.go.md|connection_test.go]] (calls)
- [[flexible-logger/flexible-logger/cmd/test-log-server/main.go.md|main.go]] (calls)
- [[flexible-logger/flexible-logger/cmd/test/main.go.md|main.go]] (calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Critical]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Debug]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.GetLevel]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Log]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Logon]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Logout]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Report]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Schedule]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.SetCallerSkip]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.SetLevel]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Stream]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Trade]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Warning]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.getEntry]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|multi.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
<!-- SYNC:END -->

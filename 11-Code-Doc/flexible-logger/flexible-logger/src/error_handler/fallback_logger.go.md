

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer.Serialize]] (method: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (imports)
- [[flexible-logger/flexible-logger/src/error_handler/error_handler_test.go.md|error_handler_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/error_handler/error_handler_test.go.md|error_handler_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|remote_notifier.go]] (calls)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|remote_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (imports)
<!-- SYNC:END -->

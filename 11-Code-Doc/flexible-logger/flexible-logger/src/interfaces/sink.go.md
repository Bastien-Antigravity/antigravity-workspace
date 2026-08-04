

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (imports)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|Sink]] (interface: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|multi.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (imports)
<!-- SYNC:END -->

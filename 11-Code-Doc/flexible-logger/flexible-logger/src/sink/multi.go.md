

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink.Write]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|MultiSink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|NewMultiSink]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)
<!-- SYNC:END -->

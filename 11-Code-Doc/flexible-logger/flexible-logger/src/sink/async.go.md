

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnError]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.worker]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnError]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.worker]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)
<!-- SYNC:END -->

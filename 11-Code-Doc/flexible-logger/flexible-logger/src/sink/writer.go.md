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
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSerializer.Serialize]] (method: calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink.Write]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (same_package)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|WriterSink]] (struct: defines_method)
<!-- SYNC:END -->

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
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (same_package)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|NewMultiSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|multi.go]] (same_package)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSerializer.Serialize]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.GetLastEntry]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.GetWriteCount]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.IsClosed]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSerializer.Serialize]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSerializer]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSerializer]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.GetLastEntry]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.GetWriteCount]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.IsClosed]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|MockSink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_BufferFull_DropsLog]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_Write]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestMultiSink_Close_AllSinksClosed]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestMultiSink_Write]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestMultiSink_ZeroSinks]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|TestWriterSink_Write]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (same_package)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|ConsoleSink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|NewConsoleSink]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|CreateLogEngine]] (function: calls)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (imports)
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|GetLogPath]] (function: calls)
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|paths.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.SetQueue]] (method: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|NewLocalNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|local_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper.SetLocalNotifQueue]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|NewCapnpSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|NewConsoleSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|NewMultiSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NewNotifLogger]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper.SetLocalNotifQueue]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|ServerCap]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (same_package)
<!-- SYNC:END -->

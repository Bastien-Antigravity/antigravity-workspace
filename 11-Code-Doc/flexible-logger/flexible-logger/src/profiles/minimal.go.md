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
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|NewLocalNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|local_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|NewConsoleSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|NewMinimalLogger]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (same_package)
<!-- SYNC:END -->

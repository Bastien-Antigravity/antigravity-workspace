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
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|LoggerMsg.Hostname]] (method: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|factory_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|factory_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|CreateLogEngine]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
<!-- SYNC:END -->

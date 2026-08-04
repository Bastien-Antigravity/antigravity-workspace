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
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|CreateLogEngine]] (function: calls)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (same_package)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|LoggerMsg.Hostname]] (method: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|DummySink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|TestCreateLogEngine_PopulatesMetadata]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|Level.String]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|Level]] (struct: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|LoggerMsg.Hostname]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|LoggerMsg.Message_]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|ReadRootLoggerMsg]] (function: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/logger/logger.go.md|logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|NewCapnpSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|capn_serializer.go]] (same_package)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|NewJSONSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|json_serializer.go]] (same_package)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer.Serialize]] (method: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|TestCapnpSerializer]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|TestJSONSerializer]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|TestTextSerializer]] (function: belongs_to)
<!-- SYNC:END -->

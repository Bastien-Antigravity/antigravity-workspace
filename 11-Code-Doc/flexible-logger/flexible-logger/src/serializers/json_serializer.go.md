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
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|JSONSerializer.Serialize]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|JSONSerializer.Serialize]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|JSONSerializer]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|JSONSerializer]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|NewJSONSerializer]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (same_package)
<!-- SYNC:END -->

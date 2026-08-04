---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer.Serialize]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/see-console-output/example_text_output.go.md|example_text_output.go]] (calls)
- [[flexible-logger/flexible-logger/cmd/see-console-output/example_text_output.go.md|example_text_output.go]] (imports)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer.Serialize]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|TextSerializer]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|truncate]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (imports)
<!-- SYNC:END -->

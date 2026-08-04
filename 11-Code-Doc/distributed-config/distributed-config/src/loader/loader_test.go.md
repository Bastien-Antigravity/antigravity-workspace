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
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetCapability]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFileSafe]] (function: calls)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFile]] (function: calls)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loader.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|MockTS]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|TestLoader]] (function: belongs_to)
<!-- SYNC:END -->

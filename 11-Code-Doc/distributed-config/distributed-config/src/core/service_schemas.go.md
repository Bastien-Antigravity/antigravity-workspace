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
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|ConfigServerCap.Validate]] (method: defines_method)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|LogServerCap.Validate]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (same_package)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|ConfigServerCap.Validate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|ConfigServerCap]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|ConfigServerCap]] (struct: defines_method)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|LogServerCap.Validate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|LogServerCap]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|LogServerCap]] (struct: defines_method)
<!-- SYNC:END -->

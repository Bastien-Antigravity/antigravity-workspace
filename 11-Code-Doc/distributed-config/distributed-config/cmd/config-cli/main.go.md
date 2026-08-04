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
- [[distributed-config/distributed-config/distributed_config.go.md|New]] (function: calls)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|main]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|printConfig]] (function: belongs_to)
<!-- SYNC:END -->

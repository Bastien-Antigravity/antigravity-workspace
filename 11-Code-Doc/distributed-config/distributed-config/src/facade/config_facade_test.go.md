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
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnLiveConfUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.SetSingle]] (method: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|NewConfig]] (function: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|TestNewConfig]] (function: belongs_to)
<!-- SYNC:END -->

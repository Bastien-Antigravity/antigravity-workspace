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
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.GetConfig]] (method: defines_method)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: defines_method)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (imports)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.GetConfig]] (method: belongs_to)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: belongs_to)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: belongs_to)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig]] (struct: defines_method)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|NewDistributedConfig]] (function: belongs_to)
<!-- SYNC:END -->

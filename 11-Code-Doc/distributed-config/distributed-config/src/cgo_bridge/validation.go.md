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
- None detected

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|main.go]] (calls)
- [[distributed-config/distributed-config/src/cgo_bridge/validation.go.md|IsValid]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/validation.go.md|ShareConfig]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/validation.go.md|ValidateMandatoryServices]] (function: belongs_to)
<!-- SYNC:END -->

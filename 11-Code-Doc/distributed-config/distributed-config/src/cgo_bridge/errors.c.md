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
- [[distributed-config/distributed-config/distconf/libdistconf/helpers.h.md|helpers.h]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|main.go]] (calls)
- [[distributed-config/distributed-config/src/cgo_bridge/errors.c.md|set_last_error]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[safe-socket/safe-socket/src/cgo_bridge/helpers.h.md|helpers.h]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|main.go]] (calls)
- [[safe-socket/safe-socket/src/cgo_bridge/errors.c.md|set_socket_error]] (function: belongs_to)
<!-- SYNC:END -->

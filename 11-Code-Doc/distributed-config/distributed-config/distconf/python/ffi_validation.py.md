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
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Close]] (function: calls)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Get]] (function: calls)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_New]] (function: calls)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distconf/python/ffi_validation.py.md|LIB_PATH]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/ffi_validation.py.md|validate_ffi]] (function: belongs_to)
<!-- SYNC:END -->

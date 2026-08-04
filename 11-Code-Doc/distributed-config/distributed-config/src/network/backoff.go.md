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
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/network/backoff.go.md|Backoff.GetDelay]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/network/backoff.go.md|Backoff.GetDelay]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/backoff.go.md|Backoff]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/network/backoff.go.md|Backoff]] (struct: defines_method)
- [[distributed-config/distributed-config/src/network/backoff.go.md|NewBackoff]] (function: belongs_to)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|backoff_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|backoff_test.go]] (same_package)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (calls)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (same_package)
<!-- SYNC:END -->

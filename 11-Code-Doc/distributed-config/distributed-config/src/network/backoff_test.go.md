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
- [[distributed-config/distributed-config/src/network/backoff.go.md|Backoff.GetDelay]] (method: calls)
- [[distributed-config/distributed-config/src/network/backoff.go.md|NewBackoff]] (function: calls)
- [[distributed-config/distributed-config/src/network/backoff.go.md|backoff.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (imports)
- [[distributed-config/distributed-config/src/interfaces/config_strategy.go.md|config_strategy.go]] (imports)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|TestBackoff_GetDelay]] (function: belongs_to)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|TestBackoff_Jitter]] (function: belongs_to)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (imports)
<!-- SYNC:END -->

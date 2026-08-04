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
- [[distributed-config/distributed-config/src/network/client.go.md|Client.Close]] (method: calls)
- [[distributed-config/distributed-config/src/network/client.go.md|Client.IsConnected]] (method: calls)
- [[distributed-config/distributed-config/src/network/client.go.md|Client.Watch]] (method: calls)
- [[distributed-config/distributed-config/src/network/client.go.md|NewClient]] (function: calls)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/network/network_resilience_test.go.md|TestNetworkResilience_Reconnection]] (function: belongs_to)
<!-- SYNC:END -->

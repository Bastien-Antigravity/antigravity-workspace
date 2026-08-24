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
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Set]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (same_package)
- [[distributed-config/distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/network/network_test.go.md|TestNetworkProtoHandler]] (function: belongs_to)
<!-- SYNC:END -->

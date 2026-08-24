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
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServer]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|TestNewGRPCServer_DockerGuard]] (function: belongs_to)
<!-- SYNC:END -->

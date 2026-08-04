---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServerWithLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (same_package)
<!-- SYNC:END -->

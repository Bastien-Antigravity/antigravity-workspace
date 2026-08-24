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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|from_str]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_full_bind_addr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|new_resolver]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|resolver.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.add_reflection]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.add_service]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.start]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.add_reflection]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.add_service]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer.start]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|GrpcServer]] (struct: defines_method)
<!-- SYNC:END -->

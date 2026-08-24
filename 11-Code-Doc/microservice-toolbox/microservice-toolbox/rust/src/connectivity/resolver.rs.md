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
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.get_primary_interface_ip]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_loopback]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_bind_addr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_full_bind_addr]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.get_primary_interface_ip]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_loopback]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_bind_addr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_full_bind_addr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|new_resolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_is_loopback]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_resolve_bind_addr_docker_suppression]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_resolve_bind_addr_native]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_resolve_full_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->
pc_server.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->

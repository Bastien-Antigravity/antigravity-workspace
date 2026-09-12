

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|resolver.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestNewResolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestResolver_ResolveBindAddr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (imports)
<!-- SYNC:END -->

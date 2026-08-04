

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfig]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|TestDockerGuard]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|TestNativeMode]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.go.md|expansion_check.go]] (imports)
<!-- SYNC:END -->

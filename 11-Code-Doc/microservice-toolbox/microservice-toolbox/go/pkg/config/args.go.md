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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine.Parse]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|CLIArgs]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (same_package)
<!-- SYNC:END -->

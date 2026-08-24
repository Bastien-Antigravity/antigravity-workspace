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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine.Parse]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine.PrintHelp]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CLIArgs]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine.Parse]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine.PrintHelp]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|CommandLine]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/CommandLine.hpp.md|MICROSERVICE_TOOLBOX_COMMAND_LINE_HPP]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (calls)
<!-- SYNC:END -->
OX_COMMAND_LINE_HPP]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (calls)
<!-- SYNC:END -->

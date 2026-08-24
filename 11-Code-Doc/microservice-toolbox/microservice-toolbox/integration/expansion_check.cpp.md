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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetLocalJSON]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetLocal]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|LoadConfig]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.cpp.md|main]] (function: belongs_to)
<!-- SYNC:END -->

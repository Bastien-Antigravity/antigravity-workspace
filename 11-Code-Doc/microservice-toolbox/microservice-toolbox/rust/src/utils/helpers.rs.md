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
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|UniLogger.new]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/helpers.rs.md|get_base_dir]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/helpers.rs.md|get_hostname]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (same_package)
<!-- SYNC:END -->

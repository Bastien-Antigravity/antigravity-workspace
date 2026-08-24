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
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|Error.from]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/config.rs.md|NatsConfig]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/config.rs.md|config.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/config.rs.md|config.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|UniLogger.new]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/connector.rs.md|connect]] (function: belongs_to)
<!-- SYNC:END -->

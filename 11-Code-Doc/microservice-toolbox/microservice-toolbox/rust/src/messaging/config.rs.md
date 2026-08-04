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
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/config.rs.md|JetStreamConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/config.rs.md|NatsConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/connector.rs.md|connector.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/connector.rs.md|connector.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/messaging/connector.rs.md|connector.rs]] (same_package)
<!-- SYNC:END -->

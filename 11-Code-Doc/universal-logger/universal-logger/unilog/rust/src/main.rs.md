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
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.add_metadata]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_config]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.log_with_metadata]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.new]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_config_update]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_config]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_metadata]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/rust/src/main.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->

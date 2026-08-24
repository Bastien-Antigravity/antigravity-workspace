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
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|UniLog_RegisterVBAWindow]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|dispatchConfigurationUpdate]] (function: belongs_to)
<!-- SYNC:END -->

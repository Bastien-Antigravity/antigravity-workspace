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
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|call_config_update_cb]] (function: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump.go.md|UniLog_RegisterVBAWindow]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump.go.md|dispatchConfigurationUpdate]] (function: belongs_to)
<!-- SYNC:END -->

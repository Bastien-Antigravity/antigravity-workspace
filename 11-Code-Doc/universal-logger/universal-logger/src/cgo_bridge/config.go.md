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
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|dispatchConfigurationUpdate]] (function: calls)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|vba_message_pump_stub.go]] (same_package)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: calls)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Get]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Get_Safe]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Set]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_OnConfigUpdate]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->

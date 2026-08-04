---
source: universal-logger/src/cgo_bridge/config.go
workspace: universal-logger
type: code-mirror
status: auto-generated
last_sync: 2026-07-04 17:57:28.905802
microservice: obsidian-brain
tags:
- '#service/obsidian-brain'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: config.go

## 📝 Description
Automatically generated mirror for `universal-logger/src/cgo_bridge/config.go`.

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

## 🔍 Implementation Details
(Add manual notes here)

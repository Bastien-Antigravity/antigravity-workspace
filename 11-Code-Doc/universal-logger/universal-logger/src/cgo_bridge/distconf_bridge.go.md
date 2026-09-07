

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|sanitizeFFIString]] (function: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_ApplyFileOverride]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Close]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Decrypt]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_FreeString]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetAddress]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetCapability]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetFullConfig]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetGRPCAddress]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetLastErrorCode]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetLastError]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Get]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_New]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_OnLiveConfUpdate]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_OnRegistryUpdate]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Set]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_ShareConfig]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Sync]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|mapErrorCode]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|setLastError]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
<!-- SYNC:END -->

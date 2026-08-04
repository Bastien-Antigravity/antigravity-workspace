

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|call_config_update_cb]] (function: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|UniLog_RegisterVBAWindow]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|dispatchConfigurationUpdate]] (function: belongs_to)
<!-- SYNC:END -->

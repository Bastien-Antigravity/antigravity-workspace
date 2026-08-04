

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|notif_callback.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump.go.md|vba_message_pump.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|vba_message_pump_stub.go]] (calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (imports)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_DECRYPTION_FAILED]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_GENERIC]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_HANDLE]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_INPUT]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_KEY_NOT_FOUND]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_NETWORK_FAILURE]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_ERR_VALIDATION_FAILED]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|DISTCONF_SUCCESS]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|GO_CGO_EXPORT_PROLOGUE_H]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|GO_CGO_PROLOGUE_H]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|call_config_update_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|call_distconf_update_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|call_notif_callback]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/libunilog/libunilog.h.md|set_last_error]] (function: belongs_to)
<!-- SYNC:END -->

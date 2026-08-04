

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (imports)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|config_handler.go]] (imports)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|FacadeSession]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Close]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Init]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|main]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|sanitizeFFIString]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->

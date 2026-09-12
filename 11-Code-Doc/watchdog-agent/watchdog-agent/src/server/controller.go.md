

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|NewController]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (calls)
<!-- SYNC:END -->

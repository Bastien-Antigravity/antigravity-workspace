

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|HealSymlinks]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|heal.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|StartNATSControlPlane]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|mfe.js]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|NewController]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/supervisor/postgres_launcher.go.md|LaunchPostgresAttempt]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|RegisterServices]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|ValidateRegistry]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|MonitorAndSupervise]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|AcquireLock]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindWorkspaceRoot]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|GetLocalIPs]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsLocal]] (function: calls)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

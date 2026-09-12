

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindPythonCmd]] (function: calls)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|RegisterServices]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|ValidateRegistry]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|resolveServiceAddr]] (function: belongs_to)
<!-- SYNC:END -->

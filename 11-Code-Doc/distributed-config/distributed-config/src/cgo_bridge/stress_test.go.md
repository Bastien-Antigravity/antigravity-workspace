

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|Get]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|Set]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|config.go]] (same_package)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|Close]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|New]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/cgo_bridge/stress_test.go.md|TestCGOBridge_StressRace]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/stress_test.go.md|iterations]] (constant: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/stress_test.go.md|numGoroutines]] (constant: belongs_to)
<!-- SYNC:END -->

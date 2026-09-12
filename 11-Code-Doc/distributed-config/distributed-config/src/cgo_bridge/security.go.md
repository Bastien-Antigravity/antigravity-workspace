

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizeString]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|bridge_test.go]] (calls)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|bridge_test.go]] (same_package)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|Decrypt]] (function: belongs_to)
<!-- SYNC:END -->

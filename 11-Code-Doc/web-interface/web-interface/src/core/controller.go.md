

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.CheckDatabase]] (method: defines_method)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.GetStatus]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.CheckDatabase]] (method: belongs_to)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.GetStatus]] (method: belongs_to)
- [[web-interface/web-interface/src/core/controller.go.md|Controller]] (struct: belongs_to)
- [[web-interface/web-interface/src/core/controller.go.md|Controller]] (struct: defines_method)
- [[web-interface/web-interface/src/core/controller.go.md|NewController]] (function: belongs_to)
- [[web-interface/web-interface/src/core/controller.go.md|StatusInfo]] (struct: belongs_to)
- [[web-interface/web-interface/src/core/controller.go.md|WebController]] (interface: belongs_to)
- [[web-interface/web-interface/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->

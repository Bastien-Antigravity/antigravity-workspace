

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleList]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleRegister]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.save]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleList]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleRegister]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.save]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Service]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|registerReq]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (same_package)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copyAssets]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copyFile]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|reorganizeAssets]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
<!-- SYNC:END -->

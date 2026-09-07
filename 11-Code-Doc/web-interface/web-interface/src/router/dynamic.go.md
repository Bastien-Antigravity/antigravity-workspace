

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|GetTopStocks]] (function: calls)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|fundamental_analysis.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls)
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|registerDynamicRoutes]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
<!-- SYNC:END -->

---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copyAssets]] (function: calls)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copy_assets.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|reorganizeAssets]] (function: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Critical]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Error]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/core/controller.go.md|NewController]] (function: calls)
- [[web-interface/web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|ConnectStockDatabase]] (function: calls)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|fundamental_analysis.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/middleware/middleware.go.md|LoggerMiddleware]] (function: calls)
- [[web-interface/web-interface/src/middleware/middleware.go.md|middleware.go]] (imports)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|RegisterPostgresBrowserRoutes]] (function: calls)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|postgres_browser.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (imports)
- [[web-interface/web-interface/src/server/facade.go.md|NewServerFacade]] (function: calls)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: calls)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Stop]] (method: calls)
- [[web-interface/web-interface/src/server/facade.go.md|facade.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|serveConcatenatedJS]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
<!-- SYNC:END -->

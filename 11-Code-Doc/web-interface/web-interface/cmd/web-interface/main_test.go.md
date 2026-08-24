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
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copy_assets.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|reorganizeAssets]] (function: calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|serveConcatenatedJS]] (function: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.AddMetadata]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Error]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.GetLevel]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.GetNotifQueue]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Info]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Log]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Logon]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Logout]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Report]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Schedule]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetCallerSkip]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetLevel]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetLocalNotifQueue]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetMetadata]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Stream]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Trade]] (method: defines_method)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copy_assets.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/copy_assets.go.md|copy_assets.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|TestConcatenatedJSEndpoints]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|TestOpenMFERegistrationAPIAndFluidLayout]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|TestSetupRoutesAndRendering]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|TestSetupRoutesMFERouting]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|init]] (function: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.AddMetadata]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.GetLevel]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.GetNotifQueue]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Log]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Logon]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Logout]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Report]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Schedule]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetCallerSkip]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetLevel]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.SetMetadata]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Stream]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Trade]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger]] (struct: belongs_to)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

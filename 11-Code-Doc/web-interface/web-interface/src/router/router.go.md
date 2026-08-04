---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|registerDynamicRoutes]] (function: calls)
- [[web-interface/web-interface/src/router/static.go.md|registerStaticRoutes]] (function: calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: belongs_to)
<!-- SYNC:END -->

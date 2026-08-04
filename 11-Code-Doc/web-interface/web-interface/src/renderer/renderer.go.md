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
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|PageData]] (struct: belongs_to)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (imports)
<!-- SYNC:END -->

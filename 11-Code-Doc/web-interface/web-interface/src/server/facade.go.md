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
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: defines_method)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Stop]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/server/facade.go.md|NewServerFacade]] (function: belongs_to)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: belongs_to)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Stop]] (method: belongs_to)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade]] (struct: belongs_to)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade]] (struct: defines_method)
<!-- SYNC:END -->

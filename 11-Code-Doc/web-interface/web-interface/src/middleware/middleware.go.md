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
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/middleware/middleware.go.md|LoggerMiddleware]] (function: belongs_to)
- [[web-interface/web-interface/src/middleware/middleware.go.md|SRFMiddleware(]] (function: belongs_to)
- [[web-interface/web-interface/src/middleware/middleware.go.md|orsMiddleware(]] (function: belongs_to)
- [[web-interface/web-interface/src/middleware/middleware.go.md|uthMiddleware(]] (function: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|postgres_browser.go]] (imports)
<!-- SYNC:END -->

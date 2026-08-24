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
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|ConnectStockDatabase]] (function: belongs_to)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|FormData]] (struct: belongs_to)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|GetTopStocks]] (function: belongs_to)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|Stock]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
<!-- SYNC:END -->
face/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
<!-- SYNC:END -->

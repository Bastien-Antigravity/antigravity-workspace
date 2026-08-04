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
- [[web-interface/web-interface/src/middleware/middleware.go.md|middleware.go]] (imports)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.ExecuteQuery]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetColumns]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetDatabases]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetSchemas]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTableData]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTables]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.getDatabase]] (method: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.switchDatabase]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.ExecuteQuery]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetColumns]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetDatabases]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetSchemas]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTableData]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTables]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.getDatabase]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler.switchDatabase]] (method: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|BrowserHandler]] (struct: defines_method)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|ColumnInfo]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|QueryRequest]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|QueryResponse]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|RegisterPostgresBrowserRoutes]] (function: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|TableData]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|TableInfo]] (struct: belongs_to)
<!-- SYNC:END -->

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
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/error_handler/error_handler_test.go.md|TestReportInternalError_WritesToStderr]] (function: belongs_to)
<!-- SYNC:END -->

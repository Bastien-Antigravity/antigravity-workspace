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
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|KillProcessGroupByID]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|KillProcessGroup]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|SetSysProcAttrGroup]] (function: belongs_to)
<!-- SYNC:END -->

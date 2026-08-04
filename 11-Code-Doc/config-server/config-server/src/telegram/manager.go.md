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
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|*toolbox_conf]] (function: belongs_to)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager]] (struct: defines_method)
- [[config-server/config-server/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to)
<!-- SYNC:END -->

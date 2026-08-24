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
- [[microservice-toolbox/microservice-toolbox/go/pkg/utils/helpers.go.md|GetHostname]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/utils/helpers.go.md|helpers.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/utils/terminal_ui.go.md|PrintInternalLog]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/utils/terminal_ui.go.md|truncate]] (function: belongs_to)
<!-- SYNC:END -->

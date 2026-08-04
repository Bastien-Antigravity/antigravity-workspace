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
- [[distributed-config/distributed-config/src/core/merger.go.md|DeepMerge]] (function: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loader.go]] (calls)
<!-- SYNC:END -->

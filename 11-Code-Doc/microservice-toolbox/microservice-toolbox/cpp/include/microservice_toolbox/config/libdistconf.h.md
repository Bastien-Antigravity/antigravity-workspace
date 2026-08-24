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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/helpers.h.md|helpers.h]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConf.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/libdistconf.h.md|GO_CGO_EXPORT_PROLOGUE_H]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/libdistconf.h.md|GO_CGO_PROLOGUE_H]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/libdistconf.h.md|call_config_update_cb]] (function: belongs_to)
<!-- SYNC:END -->

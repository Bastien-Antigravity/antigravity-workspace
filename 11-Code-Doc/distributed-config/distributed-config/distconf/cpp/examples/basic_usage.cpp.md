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
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConf.hpp]] (imports)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Decrypt]] (method: calls)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Get]] (method: calls)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: calls)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Set]] (method: calls)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distconf/cpp/examples/basic_usage.cpp.md|main]] (function: belongs_to)
<!-- SYNC:END -->

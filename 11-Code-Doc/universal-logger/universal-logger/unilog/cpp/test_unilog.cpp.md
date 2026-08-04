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
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UNILOG_CRITICAL]] (macro: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UNILOG_DEBUG]] (macro: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UNILOG_ERROR]] (macro: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UNILOG_INFO]] (macro: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UNILOG_WARNING]] (macro: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.add_metadata]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.get_config]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.get_level]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.set_config]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.set_level]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniLog.set_metadata]] (method: calls)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (imports)
- [[universal-logger/universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (same_package)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/cpp/test_unilog.cpp.md|main]] (function: belongs_to)
<!-- SYNC:END -->

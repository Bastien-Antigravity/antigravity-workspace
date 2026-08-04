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
- [[safe-socket/safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.hpp]] (imports)
- [[safe-socket/safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.receive]] (method: calls)
- [[safe-socket/safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.send]] (method: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/safesock/cpp/examples/matrix_client.cpp.md|main]] (function: belongs_to)
<!-- SYNC:END -->

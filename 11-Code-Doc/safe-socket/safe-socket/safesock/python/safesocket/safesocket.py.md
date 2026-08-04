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
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Accept]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Close]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_CreateExtended]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_GetSocketError]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Listen]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Open]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Receive]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Send]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetDeadline]] (function: calls)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetIdleTimeout]] (function: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocketConnection]] (class: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocketError]] (class: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocket]] (class: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SocketConfig]] (class: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__enter__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__exit__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__init__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|_get_last_error]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|accept]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|close]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|create]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|create_with_config]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|listen]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|open]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|receive]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|send]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|set_deadline]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|set_idle_timeout]] (function: belongs_to)
<!-- SYNC:END -->

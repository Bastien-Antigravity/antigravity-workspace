

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/cgo_bridge/errors.c.md|set_socket_error]] (function: calls)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/sanitizer.go.md|SanitizeString]] (function: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Accept]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Close]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_CreateExtended]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Create]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_FreeString]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_GetSocketError]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Listen]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Open]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Receive]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Send]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetDeadline]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetIdleTimeout]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|main]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|setError]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.hpp]] (calls)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|safesocket.py]] (calls)
<!-- SYNC:END -->

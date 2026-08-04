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
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|NewSocketClient]] (function: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|NewSocketServer]] (function: calls)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmHelloProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpHelloClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpHelloServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|tcp_server_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpHelloProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpProfile]] (function: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (calls)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateOpenSocket]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateSocket]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateWithConfig]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|Create]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultHandshakeTimeout]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultLocalHandshakeTimeout]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultShmHandshakeTimeout]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|createProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|parseSocketType]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (calls)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (same_package)
<!-- SYNC:END -->

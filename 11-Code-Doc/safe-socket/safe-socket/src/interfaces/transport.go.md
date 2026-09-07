

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/matrix_server/main.go.md|main.go]] (imports)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|socket.go]] (imports)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|handshake_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|heartbeat_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|reliable_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|TransportConnection]] (interface: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|TransportListener]] (interface: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|shm_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|tcp_client_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|tcp_server_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|tls_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|udp_profile.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|framed_tcp_client.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|framed_tcp_server.go]] (imports)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (imports)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|shm_server.go]] (imports)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|udp_client.go]] (imports)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (imports)
<!-- SYNC:END -->

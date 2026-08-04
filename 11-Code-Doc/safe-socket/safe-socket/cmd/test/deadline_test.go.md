

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetIdleTimeout]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetReadDeadline]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (same_package)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateSocket]] (function: calls)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|tcp_server_profile.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestClientDynamicDeadline]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestIdleTimeoutRefresh]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestServerConfigDeadline]] (function: belongs_to)
<!-- SYNC:END -->

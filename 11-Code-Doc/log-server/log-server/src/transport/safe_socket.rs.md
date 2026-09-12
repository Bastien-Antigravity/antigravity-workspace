

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|MAX_MESSAGE_SIZE]] (constant: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|test_heartbeat_skip]] (function: belongs_to)
<!-- SYNC:END -->

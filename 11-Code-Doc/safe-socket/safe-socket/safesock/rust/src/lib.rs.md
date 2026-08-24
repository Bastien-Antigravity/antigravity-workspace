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
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.accept]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.close]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.drop]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.get_last_error]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.listen]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.new]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.open]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.receive]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.send]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.set_deadline]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.set_idle_timeout]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.close]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.drop]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.get_last_error]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.receive]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.send]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.set_deadline]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.set_idle_timeout]] (method: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SocketConfig.default]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/safesock/rust/examples/basic_usage.rs.md|basic_usage.rs]] (calls)
- [[safe-socket/safe-socket/safesock/rust/examples/matrix_client.rs.md|matrix_client.rs]] (calls)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.accept]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.close]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.drop]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.get_last_error]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.listen]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.new]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.open]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.receive]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.send]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.set_deadline]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket.set_idle_timeout]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.close]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.drop]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.get_last_error]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.receive]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.send]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.set_deadline]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection.set_idle_timeout]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection]] (struct: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocketConnection]] (struct: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket]] (struct: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SafeSocket]] (struct: defines_method)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SocketConfig.default]] (method: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SocketConfig]] (struct: belongs_to)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|SocketConfig]] (struct: defines_method)
<!-- SYNC:END -->

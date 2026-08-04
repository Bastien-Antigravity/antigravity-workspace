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
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetTransport]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetTransport]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpClientProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpHelloClientProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpClientProfile]] (struct: defines_method)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|TcpHelloClientProfile]] (struct: defines_method)
<!-- SYNC:END -->

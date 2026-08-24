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
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetTransport]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetTransport]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetTransport]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetTransport]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsClientProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloClientProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloServerProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsServerProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsClientProfile]] (struct: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloClientProfile]] (struct: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsHelloServerProfile]] (struct: defines_method)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|TlsServerProfile]] (struct: defines_method)
<!-- SYNC:END -->

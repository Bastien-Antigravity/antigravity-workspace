

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetTransport]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpHelloProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|UdpProfile]] (struct: defines_method)
<!-- SYNC:END -->

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
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetName]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetTransport]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmHelloProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetName]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|ShmProfile]] (struct: defines_method)
<!-- SYNC:END -->

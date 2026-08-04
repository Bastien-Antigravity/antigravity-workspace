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
- [[config-server/config-server/src/store/store.go.md|Store.GetSection]] (method: defines_method)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: defines_method)
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: defines_method)
- [[config-server/config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/cmd/test/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[config-server/config-server/src/helpers/config_updates.go.md|config_updates.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/config-server/src/store/store.go.md|ConfigMap]] (struct: belongs_to)
- [[config-server/config-server/src/store/store.go.md|DeepCopy]] (function: belongs_to)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store.GetSection]] (method: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store]] (struct: belongs_to)
- [[config-server/config-server/src/store/store.go.md|Store]] (struct: defines_method)
<!-- SYNC:END -->

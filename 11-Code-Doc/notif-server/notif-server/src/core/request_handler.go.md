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
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapDeSerialize]] (method: defines_method)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapSerialize]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NewRootNotifierMsg]] (function: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Attachment]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Level]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message_]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetAttachment]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetLevel]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetMessage_]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetTags]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Tags]] (method: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|ReadRootNotifierMsg]] (function: calls)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|notifier.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/notif-server/src/core/request_handler.go.md|DeserializeNotifMsg]] (function: belongs_to)
- [[notif-server/notif-server/src/core/request_handler.go.md|NewNotifHandler]] (function: belongs_to)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapDeSerialize]] (method: belongs_to)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapSerialize]] (method: belongs_to)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler]] (struct: defines_method)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (calls)
<!-- SYNC:END -->

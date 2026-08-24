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
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.AttachmentBytes]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Attachment]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.DecodeFromPtr]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.EncodeAsPtr]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasAttachment]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasLevel]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasMessage_]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasTags]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.IsValid]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.LevelBytes]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Level]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message_Bytes]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message_]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.NewTags]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Segment]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetAttachment]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetMessage_]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetTags]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.String]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Tags]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.ToPtr]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg_Future.Struct]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (imports)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NewNotifierMsg]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NewNotifierMsg_List]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NewRootNotifierMsg]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.AttachmentBytes]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Attachment]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.DecodeFromPtr]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.EncodeAsPtr]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasAttachment]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasMessage_]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.HasTags]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.IsValid]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.LevelBytes]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Level]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message_Bytes]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Message_]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.NewTags]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Segment]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetAttachment]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetMessage_]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.SetTags]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.String]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.Tags]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg.ToPtr]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg]] (struct: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg]] (struct: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg_Future.Struct]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg_Future]] (struct: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg_Future]] (struct: defines_method)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|NotifierMsg_TypeID]] (constant: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|ReadRootNotifierMsg]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|RegisterSchema]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|schema_cd0e7dad96752db7]] (constant: belongs_to)
<!-- SYNC:END -->

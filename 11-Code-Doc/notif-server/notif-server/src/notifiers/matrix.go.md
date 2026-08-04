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
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (imports)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: belongs_to)
<!-- SYNC:END -->

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
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.SendMessage]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.buildEmail]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.dialAndSend]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.buildEmail]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.dialAndSend]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: belongs_to)
<!-- SYNC:END -->

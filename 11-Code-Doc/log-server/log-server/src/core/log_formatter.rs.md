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
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|colorize_level]] (function: calls)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|format_log_message]] (function: belongs_to)
- [[log-server/log-server/src/core/log_formatter.rs.md|test_format_log_message_basic]] (function: belongs_to)
- [[log-server/log-server/src/core/log_formatter.rs.md|test_format_log_message_with_metadata]] (function: belongs_to)
- [[log-server/log-server/src/core/log_formatter.rs.md|test_truncation]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
<!-- SYNC:END -->

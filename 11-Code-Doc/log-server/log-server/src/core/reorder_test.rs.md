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
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls)
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/reorder_test.rs.md|test_gap_timeout_recovery]] (function: belongs_to)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (imports)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/utils/helpers.rs.md|create_log_folder]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|get_exec_parent_dir]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|get_hostname]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|get_utc_timestamp]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|line_str]] (macro: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|parse_sequence_number]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|test_get_utc_timestamp]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|test_parse_sequence_number]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|test_truncate]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|truncate]] (function: belongs_to)
- [[log-server/log-server/src/utils/helpers.rs.md|validate_file_path]] (function: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (same_package)
<!-- SYNC:END -->

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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/args.py.md|args.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/args.py.md|args.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/args.py.md|parse_cli_args]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/lib_loader.py.md|CALLBACK_TYPE]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/lib_loader.py.md|lib_loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/lib_loader.py.md|lib_loader.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/merger.py.md|merger.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|get_base_dir]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|helpers.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.py.md|expansion_check.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.rs.md|expansion_check.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|AppConfig]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|__del__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_apply_cli_overrides]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_apply_file_override]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_bridge_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_check_and_add]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_get_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_load_from_file]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_load_public_key]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_normalize_ip]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_read_and_expand_yaml]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|_sync_from_bridge]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|close]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|common]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|decrypt_secret]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|deep_merge]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|env_expander]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_listen_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_mgmt_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_listen_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_local]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_rest_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_service_name]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|load_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|load_config_with_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|on_live_conf_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|on_registry_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|on_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|set_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|share_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|unmarshal_local]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|validate_unique_ports]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/test_logger.py.md|test_logger.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/test_logger.py.md|test_logger.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (calls)
<!-- SYNC:END -->

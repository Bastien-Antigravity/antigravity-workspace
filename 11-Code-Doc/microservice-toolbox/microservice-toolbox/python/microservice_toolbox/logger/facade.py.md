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
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/lib_loader.py.md|CALLBACK_TYPE]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/lib_loader.py.md|lib_loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/lib_loader.py.md|lib_loader.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|Logger]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|logger.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/logger.py.md|logger.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|LogLevel]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|from_str]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|models.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|ConfigUpdateListener]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|UniLog]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__aenter__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__aexit__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__aiter__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__anext__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__del__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__enter__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__exit__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_async_log]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_bridge_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_dispatch_log_to_cgo]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_dispatch_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_get_caller_info]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_log]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|_put]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|add_metadata]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_critical]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_debug]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_error]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_info]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_logon]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_logout]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_report]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_schedule]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_stream]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_trade]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|async_warning]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|close]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|critical]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|debug]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|error]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|get_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|get_level]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|info]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|logon]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|logout]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|on_config_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|on_notification]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|report]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|schedule]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|set_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|set_level]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|set_metadata]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|stream]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|trade]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|warning]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/test_logger.py.md|test_logger.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (calls)
<!-- SYNC:END -->

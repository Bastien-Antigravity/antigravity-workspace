

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|ManagedConnection]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|reconnect]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|MaxRetriesReachedError]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|ConnectionMode]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|NetworkManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|connect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|connect_blocking]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|connect_non_blocking]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|connect_with_retry]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|establish_connection]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|get_next_delay]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|new_critical_strategy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|new_network_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|new_network_manager_with_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|new_performance_strategy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|new_standard_strategy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|run_reconnect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/test_logger.py.md|test_logger.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/test_logger.py.md|test_logger.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (calls)
<!-- SYNC:END -->

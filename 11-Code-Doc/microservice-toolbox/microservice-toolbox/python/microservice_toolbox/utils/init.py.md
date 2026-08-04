

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/lib_loader.py.md|lib_loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/lib_loader.py.md|load_libdistconf]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|load_config]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|set_logger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|UniLog]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|_find_nearest_venv]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|bootstrap.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|bootstrap.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|find_vault_root]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|get_venv_python]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|redirect_working_directory]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init_microservice]] (function: belongs_to)
<!-- SYNC:END -->

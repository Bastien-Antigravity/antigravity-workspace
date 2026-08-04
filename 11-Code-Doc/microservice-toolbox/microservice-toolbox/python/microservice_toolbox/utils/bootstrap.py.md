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
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|_find_nearest_venv]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|bootstrap_microservice]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|find_vault_root]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|get_venv_python]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|redirect_working_directory]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (same_package)
<!-- SYNC:END -->

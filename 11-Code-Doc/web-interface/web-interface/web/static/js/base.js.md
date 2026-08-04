---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/html/CV.html.md|#sidebar (div)]] (element: calls)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.closeSidebar]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.closeSidenav]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.getSidebarWidth]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.init]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.loadSavedTheme]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.openSidebar]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.openSidenav]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.setupClock]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.setupResponsiveTriggers]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.showLoginModal]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleDropdown]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleSidebar]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleSidenav]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleTheme]] (method: defines_method)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarSidebar (img)]] (element: calls)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarTop (img)]] (element: calls)
- [[web-interface/web-interface/web/templates/base.html.md|IS_LOGGED_IN]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.closeSidebar]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.closeSidenav]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.getSidebarWidth]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.init]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.loadSavedTheme]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.openSidebar]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.openSidenav]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.setupClock]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.setupResponsiveTriggers]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.showLoginModal]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleDropdown]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleSidebar]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleSidenav]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController.toggleTheme]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|BaseUIController]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/base.js.md|CloseNav]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|OpenCloseNav]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|OpenNav]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|drop_down_func_id]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|toggleTheme]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|update]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|w3_OpenClose]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|w3_close]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|w3_open]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/database-explorer.js.md|database-explorer.js]] (calls)
- [[web-interface/web-interface/web/static/js/database-explorer.js.md|database-explorer.js]] (same_package)
<!-- SYNC:END -->

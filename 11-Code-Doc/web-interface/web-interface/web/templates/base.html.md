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
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|RtTaAnalyst.html]] (calls)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|TAIndicatorsAll.html]] (calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|TradedVolume.html]] (calls)
- [[web-interface/web-interface/web/static/analyst/getConfigData.js.md|getConfigData.js]] (calls)
- [[web-interface/web-interface/web/static/js/base.js.md|base.js]] (calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/templates/base.html.md|#Algo (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Architecture (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Crypto_Analysis (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Machine_Learning (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#MicroServices (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Misc (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Other_Analysis_Sidebar (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#OverlayNav (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#OverlaySide (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Overview (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Sidebar (nav)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Sidenav (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Stocks_Analysis_Sidebar (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Technical_Analysis (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarSidebar (img)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarTop (img)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#date_time (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#main (main)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-nav-accordion (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#partOfProject (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#sidebar-close-mobile (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#sidebar-toggle (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#theme-toggle (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|IS_LOGGED_IN]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_WSS_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|updateClock]] (function: belongs_to)
<!-- SYNC:END -->

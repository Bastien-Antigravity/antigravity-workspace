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
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.clear]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.renderVolumeProfileOverlay]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.setVolumeProfile]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.setupResizeListener]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.updateMicroprice]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.updateOBI]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|C.update]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.clear]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.renderVolumeProfileOverlay]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.setVolumeProfile]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.setupResizeListener]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.updateMicroprice]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.updateOBI]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|cytoscape_part10.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part23.js.md|cytoscape_part23.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part3.js.md|cytoscape_part3.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part9.js.md|cytoscape_part9.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|layout_part6.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/EventBus.js.md|EventBus.js]] (calls)
<!-- SYNC:END -->

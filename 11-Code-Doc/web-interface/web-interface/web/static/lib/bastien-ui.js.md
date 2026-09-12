

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass.init]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass.start]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.autoInit]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getInstance]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.registerAll]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/atoms/MetricBadge.js.md|MetricBadge.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/atoms/StatusIndicator.js.md|StatusIndicator.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/organisms/DataGrid.js.md|DataGrid.js]] (imports)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (imports)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.js]] (imports)
- [[web-interface/web-interface/web/static/lib/utils/EventBus.js.md|EventBus.js]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass.init]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass.start]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|BastienUIClass]] (class: defines_method)
<!-- SYNC:END -->

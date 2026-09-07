

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard.onMessage]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard.renderRow]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (same_package)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (same_package)
- [[web-interface/web-interface/web/static/js/prism.js.md|prism.js]] (calls)
- [[web-interface/web-interface/web/static/js/prism.js.md|prism.js]] (same_package)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard.onMessage]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard.renderRow]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|TradedVolumeDashboard]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|onmessage]] (function: belongs_to)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onclose]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onerror]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onmessage]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onopen]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (same_package)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.connect]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.reconnect]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.sendMessage]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (imports)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.js]] (imports)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.connect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.reconnect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient.sendMessage]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient]] (class: belongs_to)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|WebSocketClient]] (class: defines_method)
<!-- SYNC:END -->

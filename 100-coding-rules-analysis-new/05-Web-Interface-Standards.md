# 🌐 Web Interface Standards (HTML/CSS/JS)
*Focus areas: Administrative Dashboards, Realtime Charting, Web UIs*

## 1. JavaScript: Object-Oriented Event Binding
Websocket connections and chart components are built as strict ES6 classes.
- **Singleton Pattern**: Websocket managers (e.g., `TA_WebSocketBindingManager`) implement singletons to prevent zombie connection leaks during hot-reloads and UI state changes.
  ```javascript
  if (TA_WebSocketBindingManager.instance) { return TA_WebSocketBindingManager.instance; }
  ```
- **Custom Event Routing**: Rather than standard `addEventListener` logic, components use a unique binding map (`bindingsOnMessage.set(id, object[methodName].bind(object))`) generating specific IDs. This ensures components can cleanly attach and detach from shared websockets.

## 2. HTML: Template Injection & Bootstrap Grids
- **Go HTML Templates**: HTML files are built for backend injection using Go's `html/template` package (`{{define "content"}}`, `{{template "connectionLogModal"}}`).
- **Semantic Structure**: Heavy reliance on Bootstrap classes (`card`, `row`, `col-md-4`, `shadow-sm`, `rounded-lg`).
- **Emoji Visual Identifiers**: Dashboards utilize consistent emojis in headers for rapid visual parsing (`🚀 Top Gainers`, `📢 Abnormal Volume`, `🩺 Backend Health`).

## 3. JS Visual Dividers
To handle large UI logic files, JavaScript code utilizes an unmistakable double-thick divider to separate core class definitions:
`////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////`

## 4. Modular CSS
Styling is kept minimal in the HTML layer. Instead, layout-specific styling is extracted into dedicated external stylesheets (e.g., `market-observer.css`, `ta-indicators.css`) while relying on `base.css` for cross-fleet UI consistency.

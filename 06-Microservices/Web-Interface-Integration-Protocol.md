---
microservice: web-interface
type: protocol
status: active
tags:
- '#service/web-interface'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🌐 Web Interface Integration Protocol

This protocol defines how to centralize microservice management, monitoring, and real-time data visualization within the primary `web-interface` dashboard.

## 1. The Gateway Plugin Pattern

To keep the `web-interface` maintainable, every microservice integration MUST follow the **Plugin Pattern**. Instead of adding logic directly to `main.go`, create a dedicated integration package.

### File Structure
```text
web-interface/
  src/
    integrations/
      {service_name}/
        controller.go   # REST/WebSocket handlers
        grpc_client.go  # Communication with the microservice
        router.go       # Route registration
```

## 2. Integration Workflow

### Step 1: gRPC Client Initialization
Use the `microservice-toolbox` to resolve the service address and initialize a gRPC client. Do NOT hardcode IPs.

```go
// Resolved via toolbox
addr, _ := toolbox.GetGRPCListenAddr("data-ingestor")
conn, _ := grpc.Dial(addr, grpc.WithInsecure())
client := pb.NewControlServiceClient(conn)
```

### Step 2: Route Registration
Implement a `RegisterRoutes` function that takes the main `http.ServeMux`.

```go
func RegisterRoutes(mux *http.ServeMux, client pb.ControlServiceClient) {
    mux.HandleFunc("/api/v1/ingestor/start", handleStart(client))
    mux.HandleFunc("/ws/ingestor/logs", handleLogStream(client))
}
```

### Step 3: WebSocket Multiplexing (Live Streams)
For real-time data (prices, logs), the backend should:
1.  Open a gRPC stream to the microservice.
2.  Upgrade the browser request to a WebSocket.
3.  Forward gRPC messages to the WebSocket in a non-blocking loop.

## 3. Frontend Standards

The UI design is optimized for a premium, low-fatigue developer experience. Full visual guidelines, styling tokens, and layout schemas are formalized in [PAGE_RENDERING.md](../../web-interface/PAGE_RENDERING.md).

### Visual Identity & Theme Architecture
*   **Theme Tokens**: Style rules and colors reference CSS variables defined in `/web/static/lib/tokens/design-tokens.css`. Light/dark variations are defined as overrides in `/web/static/lib/theme/themes.css`. Hardcoded colors are strictly prohibited.
*   **Default Theme**: Dark theme uses soft, non-fatiguing deep blue-gray backgrounds (`hsl(222, 25%, 10%)`).
*   **Light Theme**: Light theme overrides backgrounds with clean, non-glaring warm gray-whites (`hsl(210, 15%, 93%)`).
*   **Typography**: Adheres to the strict three-family font system defined in [PAGE_RENDERING.md](../../web-interface/PAGE_RENDERING.md):
    *   `var(--font-display)` (`Outfit`): Used for headings, main titles, and KPI stats metrics.
    *   `var(--font-sans)` (`Inter`): Used for paragraphs, forms, UI menus, and buttons.
    *   `var(--font-mono)` (`JetBrains Mono` / `Fira Code`): Used for numbers, code blocks, raw data tables (depth/prices), and inputs to prevent layout shifting. AI agents must utilize token variables instead of raw family names.

### Component System
*   **Layout Wrapper**: Child dashboard pages must omit `<html>`, `<head>`, `<body>`, and layout headers. They are encapsulated inside the `{{define "content"}}` block, wrapped in `.bastien-container`, and structured using Bootstrap grids (`.row`, `.col-lg-*`).
*   **Panels & Cards**: Dashboards utilize the glassmorphic `.bastien-card--glass` layout with internal padding segments (`.bastien-card__header`, `.bastien-card__body`).
*   **Forms & Fields**: Input controls and dropdown select fields must use `.bastien-input` and `.bastien-form-group` classes.
*   **Buttons**: Trigger controls use `.bastien-btn` with state modifiers: `--primary` (blue), `--secondary` (glass), and `--danger` (red).
*   **Icons**: Consistent Font Awesome v4.7 (`fa fa-*`) icon utilization is required:
    *   `fa-terminal` / `fa-code`: Code consoles, shell tools.
    *   `fa-cogs` / `fa-sliders`: Configuration panels.
    *   `fa-bar-chart` / `fa-line-chart`: Metrics and statistics.
    *   `fa-moon-o` / `fa-sun-o`: Theme toggling.
*   **Dynamic Component Registration**: UI widgets bind interaction dynamically through `data-component="..."` declarations processed by [bastien-ui.js](../../web-interface/web/static/lib/bastien-ui.js). Inline scripting and inline styling are not allowed.

### UI Template Integration
1.  Add the page HTML to `web/html/{page_name}.html`, defining the layout content block via `{{define "content"}}`.
2.  Register the endpoint in `src/router/static.go` with `renderer.RenderPage(w, r, "base", "{page_name}", nil, appConfig)` to wrap the page within the dashboard layout frame.


## 4. Service Discovery Truth
The `web-interface` MUST be the only service that has an "Overview" of the entire fleet. It uses the `distributed-config` bridge to discover the `capabilities` of every running node and dynamically renders its UI based on what is currently active in the ecosystem.

## 5. Config Server Management Integration
The `web-interface` features a dedicated **Configuration Server Manager** admin dashboard that acts as the central client for `config-server` remote functionalities.

### Architecture
- **gRPC Target**: Connects to the shadow gRPC sync port of `config-server` (default `127.0.0.1:3307`).
- **Client implementation**: `src/config_browser/client.go` encapsulates the gRPC `ConfigControlServiceClient` methods mapping to the `ConfigController` interface definitions.
- **Controller and Handlers**: `src/config_browser/controller.go` handles route binding and requests:
  - `GET /ConfigBrowser`: Renders the main config browser admin page.
  - `POST /api/v1/config_browser/set`: Updates/inserts an override parameter in memory.
  - `POST /api/v1/config_browser/reload`: Resets memory state and reloads configuration from the base YAML baseline.
  - `POST /api/v1/config_browser/persist`: Commits current overrides to disk.
- **UI View**: `web/html/ConfigBrowser.html` presents status, active fleet clients, and accordion-based editors.

---
*Last Updated: 2026-06-19*
*See also: [[Microservice-Startup-Protocol]], [[OpenMFE-Integration-Protocol]]*

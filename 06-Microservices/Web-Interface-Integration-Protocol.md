---
microservice: web-interface
type: protocol
status: active
tags:
- '#service/web-interface'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
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

### The "Service Card" Pattern
Every microservice integrated into the dashboard should provide a **Service Card** in the UI:
*   **Status Indicator**: (Green/Red) based on `/health` gRPC check.
*   **Quick Actions**: Start/Stop/Restart buttons.
*   **Live Metrics**: Small sparkline or text update for primary data (e.g., "Active Brokers: 5").

### UI Template Integration
1.  Add the service HTML to `web/html/segments/`.
2.  Include it in the main dashboard via the `web-interface` template engine.

## 4. Service Discovery Truth
The `web-interface` MUST be the only service that has an "Overview" of the entire fleet. It uses the `distributed-config` bridge to discover the `capabilities` of every running node and dynamically renders its UI based on what is currently active in the ecosystem.

---
*Last Updated: 2026-05-09*
*See also: [[Microservice-Startup-Protocol]]*

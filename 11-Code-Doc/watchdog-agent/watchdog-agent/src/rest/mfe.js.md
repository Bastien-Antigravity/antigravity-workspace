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
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.apeAttribute(va]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.apeHTML(va]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.connectedCallback]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dAll() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dEvents() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dStatus() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.disconnectedCallback]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.playServices() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.playStatus() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.renderSkeleton]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.rtPostgres() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.tartAll() ]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.tartService(na]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.apeAttribute(va]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.apeHTML(va]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.connectedCallback]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dAll() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dEvents() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.dStatus() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.disconnectedCallback]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.playServices() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.playStatus() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.renderSkeleton]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.rtPostgres() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.tartAll() ]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.tartService(na]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE]] (class: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE]] (class: defines_method)
<!-- SYNC:END -->

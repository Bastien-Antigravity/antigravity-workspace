---
microservice: market-observer
type: service-hub
status: active
tags:
- '#service/market-observer'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Market-Observer

*Real-time exchange connectivity and orderbook tracking.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 market-observer](https://github.com/Bastien-Antigravity/market-observer)
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/market-observer/)
- **Action Plan**: [📅 Local TODO](https://github.com/Bastien-Antigravity/market-observer/blob/develop/TODO.md)

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Go-Systems-Specialist|Go-Systems]]
- **Data Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Timescale-Data-Specialist|Timescale-Data]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/market-observer"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*

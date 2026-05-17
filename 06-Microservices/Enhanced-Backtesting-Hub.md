---
microservice: enhanced-backtesting
type: service-hub
status: active
tags:
- '#service/enhanced-backtesting'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Enhanced-Backtesting

*High-Performance Strategy Backtesting Engine with ArcticDB (LMDB) Persistence.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 enhanced-backtesting](https://github.com/Bastien-Antigravity/enhanced-backtesting)
- **Behavior Specs**: [[Backtest-Engine|Backtest Engine]]
- **Storage Profile**: Uses ArcticDB (LMDB) for tick-data persistence.

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Python-Quant]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/enhanced-backtesting"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

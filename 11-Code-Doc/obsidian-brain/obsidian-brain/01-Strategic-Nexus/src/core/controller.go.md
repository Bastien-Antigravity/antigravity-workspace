

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md| string) string ]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|, prefix string)]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|DBManager]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|EvolutionPipeline]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|erns(content string) []] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|ontent string) []] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|string) string ]] (function: belongs_to)
<!-- SYNC:END -->

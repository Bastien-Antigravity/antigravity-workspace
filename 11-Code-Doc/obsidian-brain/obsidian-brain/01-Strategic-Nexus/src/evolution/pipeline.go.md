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
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.EvaluateFitness]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.MutatePrompt]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|DBManager]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.EvaluateFitness]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.MutatePrompt]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline]] (struct: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline]] (struct: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|NewEvolutionPipeline]] (function: belongs_to)
<!-- SYNC:END -->

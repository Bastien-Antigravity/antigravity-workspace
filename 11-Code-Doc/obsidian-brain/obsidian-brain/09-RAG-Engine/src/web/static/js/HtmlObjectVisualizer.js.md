

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|transform]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.push]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._renderTree]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._showInfo]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._transformDomToTree]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer.render]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|persona_extractor.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lifecycle/unlock_vault.py.md|unlock_vault.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/joint_audit_purger.py.md|joint_audit_purger.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._renderTree]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._showInfo]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer._transformDomToTree]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer.render]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer]] (class: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: belongs_to)
<!-- SYNC:END -->
in/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer]] (class: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)

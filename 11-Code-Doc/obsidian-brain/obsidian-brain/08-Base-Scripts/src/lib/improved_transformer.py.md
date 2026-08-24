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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|add]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|CodeTransformer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|ImportVisitor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|UsageTransformer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_clean_shebang_and_encoding]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_class_and_method_docstrings]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_docstring_empty_line]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_granular_imports]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_granular_imports_regex]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_logger_formatting]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_method_dividers]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|_ensure_triple_block_docstring]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|replace_f]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|replace_s]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|transform]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|visit_Attribute]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|visit_ImportFrom]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|visit_Import]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|visit_Name]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer.js]] (calls)
<!-- SYNC:END -->



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|RAGControlServiceServicer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|add_RAGControlServiceServicer_to_server]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|rag_control_pb2_grpc.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|BuildIndex]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|GetBrainStats]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|GetStatus]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|IndexDirectory]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|IndexFile]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|RAGControlServiceImpl]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|ResetIndex]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|SyncDocs]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|start_grpc_server]] (function: belongs_to)
<!-- SYNC:END -->

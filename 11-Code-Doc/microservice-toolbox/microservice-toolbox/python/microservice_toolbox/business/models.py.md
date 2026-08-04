

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|BotCommand_CommandType.Enum]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Aggressor]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEventType]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEvent]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OHLCV]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OrderBookLevel]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OrderBook]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Quote]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|SignalType]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Signal]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Trade]] (class: belongs_to)
<!-- SYNC:END -->
g
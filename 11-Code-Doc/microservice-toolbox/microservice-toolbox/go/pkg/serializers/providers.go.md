

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer.Marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer.Unmarshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Marshal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Unmarshal]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer.Marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer.Unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|BinSerializer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Marshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer.Unmarshal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|JSONSerializer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewBinSerializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/providers.go.md|NewJSONSerializer]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|serializer_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/serializers/serializer_test.go.md|serializer_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_con.go.md|matrix_con.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_gen.go.md|matrix_gen.go]] (calls)
<!-- SYNC:END -->

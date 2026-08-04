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
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|args.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {._live_conf_update<F]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {._registry_update<F]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_and_expand_yaml(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_config(p]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_from_file(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_public_key(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.are_config(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.crypt_secret(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ep_merge(d]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.lidate_unique_ports(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.marshal_local<T]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.mmon(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.nc_from_bridge(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.op(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ply_cli_overrides(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ply_file_override(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_addr(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_config(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_grpc_listen_addr(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_grpc_mgmt_addr(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_listen_addr(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_local(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_logger(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_rest_addr(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_service_name(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_value(&]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ternal_cb(_]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ternal_reg_cb(_]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/merger.rs.md|merger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.rs.md|expansion_check.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md| {
     ]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|_file_returns_error() {
       ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|_local() {
   ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|_local_empty() {
   ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ad_config(p]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ad_config_with_logger(p]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ansion() {
       ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|arshal_local() -> Re]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|c_missing_returns_error() {
   ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ecrypt_enc_block_errors_without_bridge() {
 ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|nfig_from_file() {
       ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ogger() {
     ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {._live_conf_update<F]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {._registry_update<F]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_and_expand_yaml(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_config(p]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_from_file(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ad_public_key(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.are_config(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.crypt_secret(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ep_merge(d]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.lidate_unique_ports(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.marshal_local<T]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.mmon(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.nc_from_bridge(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.op(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ply_cli_overrides(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ply_file_override(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_addr(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_config(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_grpc_listen_addr(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_grpc_mgmt_addr(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_listen_addr(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_local(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_logger(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_rest_addr(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_service_name(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.t_value(&]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ternal_cb(_]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {.ternal_reg_cb(_]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|pConfig {]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|ress_resolution() {
   ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|rride_targets_single_capability() {
       ]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|st_config_deep_merge()]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|st_decrypt_plaintext_passthrough()]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|t_live_cb()]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|t_reg_cb()]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->

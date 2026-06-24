# AI Dependency Atlas Validation Report

**Overall: PASS**

## Recomputed metrics

| Metric | Value |
|---|---:|
| Nodes | 320 |
| Typed edges | 1225 |
| References | 63 |
| Layers | 12 |
| Unique definitions | 320 |
| Boilerplate definitions | 0 |
| Reference coverage | 100.0% |
| Rich-node coverage | 100.0% |
| Non-system terminal nodes | 0 |
| Manually curated supporting context | 42 |
| Graph-derived supporting context | 278 |
| Maximum dependency depth | 19 |
| Same-layer edges | 294 |

## Checks

| Check | Result | Details |
|---|---|---|
| `json_schema` | PASS | issues=0 |
| `unique_identifiers` | PASS | issues=0 |
| `layer_membership` | PASS | issues=0 |
| `edge_integrity` | PASS | issues=0, same_layer_edges=294 |
| `reference_integrity` | PASS | issues=0 |
| `acyclic_graph` | PASS | issues=0, max_depth=19 |
| `rich_content` | PASS | unique_definitions=320, boilerplate_definitions=0, incomplete_fields=0 |
| `terminal_semantics` | PASS | issues=0, terminal_nodes=19, non_system_terminal_nodes=0 |
| `declared_modern_coverage` | PASS | present=18, required=18 |
| `reproducible_statistics` | PASS | issues=0 |

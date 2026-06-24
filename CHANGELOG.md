# Changelog

## 2.0.0-draft — 2026-06-22

### Rebuilt ontology

- Expanded the atlas to 320 family-level concepts across 12 layers.
- Added typed, strength-labeled, justified dependency edges.
- Added dedicated nodes for scaling laws, compute-optimal training, GRPO, RLVR, inference-time scaling, Tree/Graph-of-Thought, neural architecture search, output watermarking, content provenance, sim-to-real, domain randomization, Mixture-of-Depths, structured outputs, formal verification, encoder-only transformers, Transformer–SSM hybrids, diffusion language models, VLA models, model merging, and checkpoint composition.
- Rewired reusable memory, reasoning, training, alignment, and infrastructure concepts into downstream consumers.
- Eliminated legacy boilerplate concept definitions.

### Honest completeness contract

- Replaced the unbounded “complete” claim with a family-level scope statement and explicit exclusions.
- Added node-level editorial provenance distinguishing curated supporting context from graph-derived supporting context.
- Added a machine-readable content audit that reports graph-derived prose patterns and reference concentration rather than concealing them.

### Project tooling

- Made `data/atlas.json` the canonical source of truth.
- Added a Draft 2020-12 JSON Schema.
- Added semantic validation, DAG checking, terminal-topology checking, modern-coverage checks, and reproducible statistics.
- Added a deterministic standalone HTML builder and SHA-256 build manifest.
- Added automated tests and a GitHub Actions workflow.
- Added scope, architecture, editing, and build documentation.

### Viewer

- Added Explore and Compare modes.
- Added direct/full lineage tracing, focus mode, search, filters, presets, and orientation reversal.
- Added typed-edge details, dependency rationales, consumer tracing, references, scope/validation modal, JSON export, and editorial-status badges.

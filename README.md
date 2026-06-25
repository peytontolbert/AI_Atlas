# The Dependency Atlas of Artificial Intelligence

A standalone, interactive dependency map of artificial intelligence organized as a **family-level ontology** rather than a list of products or model releases.

> **Status:** family-level scope complete, not exhaustive.  
> The atlas is complete only against the scope and quality contract documented in [`docs/SCOPE.md`](docs/SCOPE.md). It does not claim to enumerate every paper, named model, dataset, benchmark, implementation, vendor feature, or emerging term.

## Current build

| Measure | Value |
|---|---:|
| Concepts | 320 |
| Typed dependency edges | 1,225 |
| Layers | 12 |
| Reference records | 63 |
| Unique concept definitions | 320 |
| Legacy boilerplate definitions | 0 |
| Reusable non-system nodes without consumers | 0 |
| Maximum dependency depth | 19 |

The ontology includes mathematical and computational foundations, data representations, learning paradigms, objectives, mechanisms, architecture families, training and adaptation, memory and retrieval, reasoning and agency, alignment and assurance, infrastructure, and end systems.

## What “complete” means here

This release uses a bounded definition of completeness:

1. Every major enduring family in the declared scope has a first-class node.
2. The omissions identified in the v1 review—scaling laws, compute-optimal training, GRPO, RLVR, inference-time search, Tree/Graph-of-Thought, neural architecture search, watermarking and provenance, sim-to-real, domain randomization, adaptive depth, structured outputs, and formal verification—are represented directly.
3. Every dependency is typed, strength-labeled, and justified.
4. Every concept has a unique definition, a declared editorial status, at least one reference pointer, and an explicit terminal/non-terminal interpretation.
5. The graph passes schema, identifier, edge, reference, layer-direction, cycle, rich-content, terminal-semantics, modern-coverage, and reproducible-statistics checks.

It **does not** mean that all AI research has been exhaustively cataloged. The viewer exposes the scope statement, known exclusions, validation metrics, and editorial provenance rather than hiding them behind a “complete” label.

## Editorial provenance

All 320 concept definitions are concept-specific. Supporting sections are labeled at node level:

- `curated`: definition, role summary, examples, and limitations were manually authored for this draft.
- `definition_curated_context_graph_derived`: the definition is concept-specific, while the role summary, downstream examples, and baseline limitation note are generated from the validated graph.

The build currently contains **42 curated supporting-context nodes** and **278 graph-derived supporting-context nodes**. This distinction is deliberate. Graph-derived context is useful for tracing lineage, but it is not presented as equivalent to a full textbook treatment. See [`dist/content_audit_report.md`](dist/content_audit_report.md).

## Open the atlas

Run the local server:

```bash
make serve
```

Then open:

```text
http://127.0.0.1:8088/
```

The server redirects to the generated standalone viewer at `dist/ai_dependency_atlas_v2.html`. The viewer is fully self-contained: no package manager, CDN, font download, or network request is required for the interface. Reference links open only when selected.

You can still open the generated file directly in a modern browser if preferred:

```text
dist/ai_dependency_atlas_v2.html
```

Core interactions:

- **Explore:** select a concept to trace its complete or direct prerequisite substrate and downstream consumers.
- **Compare:** select two concepts to compare shared and unique dependency substrate.
- **Search and filters:** query labels, aliases, definitions, tags, layers, and maturity.
- **Focus lineage:** dim concepts outside the active trace.
- **Reverse orientation:** switch between systems-first and foundations-first reading.
- **Scope & validation:** inspect the exact completeness contract, exclusions, and editorial disclosure.
- **Export JSON:** download the canonical embedded data from the viewer.

## Reproduce the build

Python 3.10+ is recommended.

```bash
python -m pip install -r requirements-dev.txt
make validate
make build
make test
```

Equivalent direct commands:

```bash
python tools/validate_atlas.py
python tools/audit_content.py
python tools/build_atlas.py
python tools/generate_audit_packets.py
python tools/compile_source_audit_ledgers.py
python tools/validate_source_audit.py
python -m unittest discover -s tests -v
```

Optional browser-level smoke test:

```bash
python -m pip install -r requirements-browser.txt
playwright install chromium
make smoke
```

The smoke test verifies rendering, Explore mode, Compare mode, shared-substrate highlighting, scope disclosures, search, SVG edges, and browser-console cleanliness. It writes `dist/browser_smoke_report.json` and refreshes the preview image.

The build stops on validation failure. `dist/build_manifest.json` records SHA-256 hashes for all canonical inputs and generated outputs.

## Hugging Face dataset and universe export

Build a layout-ready atlas universe plus a single multi-config Hugging Face dataset:

```bash
make hf-dataset
```

This writes JSONL configs for canonical nodes, edges, references, sentence reviews, edge reviews, node packets, course lessons, and universe graph data under `exports/huggingface/ai_atlas_dataset_v1/`. If the selected Python interpreter has `pyarrow`, it also writes parquet copies.

To push the generated dataset folder:

```bash
HF_DATASET_ID=PeytonT/ai_atlas PYTHON=python make hf-dataset-push
```

See [`docs/HUGGINGFACE_AND_UNIVERSE.md`](docs/HUGGINGFACE_AND_UNIVERSE.md) for the dataset configs and the interactive-universe layout.

## Repository layout

```text
ai_dependency_atlas/
├── data/
│   └── atlas.json                  # canonical source of truth
├── schema/
│   └── atlas.schema.json           # JSON Schema, Draft 2020-12
├── tools/
│   ├── validate_atlas.py           # structural and semantic validation
│   ├── audit_content.py            # editorial-provenance audit
│   ├── build_atlas.py              # deterministic standalone HTML build
│   └── smoke_test_viewer.py        # optional Playwright browser test
├── tests/
│   └── test_atlas.py               # integrity, scope, and build tests
├── docs/
│   ├── SCOPE.md
│   ├── ARCHITECTURE.md
│   └── EDITING.md
├── .github/workflows/validate.yml  # CI validation/build/test workflow
├── viewer.template.html            # application shell with JSON placeholder
├── requirements-dev.txt
├── requirements-browser.txt
├── Makefile
├── CHANGELOG.md
└── dist/
    ├── ai_dependency_atlas_v2.html
    ├── ai_dependency_atlas_v2_data.json
    ├── validation_report.{json,md}
    ├── content_audit_report.{json,md}
    ├── source_audit_report.{json,md}
    ├── strict_blocker_report.{json,md}
    ├── browser_smoke_report.json
    ├── ai_dependency_atlas_v2_preview.png
    └── build_manifest.json
```

## Relationship semantics

An edge points from a higher-level concept to a declared dependency. It carries one of these relationship types:

| Type | Meaning |
|---|---|
| `requires` | rests on a formal or computational capability |
| `uses` | incorporates a reusable ingredient |
| `represents_with` | consumes, emits, or organizes a representation |
| `optimizes_for` | is learned, selected, or assessed through an objective |
| `trained_under` | follows a learning paradigm |
| `specializes` | extends or narrows an architecture family |
| `composes` | is assembled from a mechanism or model component |
| `adapts` | changes, compresses, or combines parameters |
| `retrieves_from` | stores, selects, or obtains information |
| `searches_with` | explores alternatives through a search process |
| `verifies_with` | checks candidates against evidence or constraints |
| `evaluates_or_constrains` | measures, governs, audits, or limits behavior |
| `operationalizes` | turns a concept into a scalable deployable capability |
| `applies` | integrates a concept into an end-to-end system |

Strength is separately labeled `core`, `common`, or `optional`. Same-layer edges are permitted for specialization and composition; the atlas is a directed acyclic graph, not a perfectly stratified stack.

## Source policy

References are pointers to relevant primary papers, standards, surveys, or foundational textbooks. Every node has at least one reference pointer, but a pointer is **not** a sentence-level citation audit. Broad foundational sources are deliberately reused across related concepts. Node-specific sourcing is an editorial expansion target documented by the content audit.

For the stricter standard required to make a sentence-level fact-checking claim, see [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md). Run `make source-audit` for audit-record coverage and `make strict-blockers` for the remaining ambiguous/unsupported records that block a strict fact-checking claim. For the roadmap toward bounded exhaustive coverage, see [`docs/EXHAUSTIVENESS_ROADMAP.md`](docs/EXHAUSTIVENESS_ROADMAP.md).

## Contribution standard

A proposed node should represent a reusable conceptual family with a distinct dependency pattern. It should not be added only because a named product, model release, framework, or paper exists. See [`docs/EDITING.md`](docs/EDITING.md) for the required schema and quality checklist.

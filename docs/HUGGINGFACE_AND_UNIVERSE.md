# Hugging Face Dataset and Atlas Universe

The AI Dependency Atlas can be packaged as one Hugging Face dataset and as a layout-ready interactive universe. The exporter always writes JSONL data files and also writes parquet when the selected Python interpreter has `pyarrow` installed.

## Dataset Shape

Use one dataset repository with multiple configs:

| Config | Purpose |
|---|---|
| `nodes` | Canonical atlas concept nodes from `data/atlas.json`. |
| `edges` | Typed dependency edges. |
| `references` | Source pointer records. |
| `source_sentence_reviews` | Sentence-level source audit records. |
| `edge_reviews` | Edge audit records. |
| `node_packets` | Per-node audit packets as compact JSON. |
| `course_lessons` | Markdown course and lesson files. |
| `universe_nodes` | Layout-ready concept nodes for an interactive universe. |
| `universe_edges` | Layout-ready dependency edges for an interactive universe. |

This keeps the atlas as a single dataset while preserving separable views for graph ML, retrieval, audit review, and teaching workflows.

## Local Build

Optional parquet/push dependencies:

```bash
python -m pip install -r requirements-hf.txt
```

Build artifacts:

```bash
make universe
make hf-dataset
```

Outputs:

```text
exports/universe/
├── nodes.jsonl
├── edges.jsonl
└── manifest.json

exports/huggingface/ai_atlas_dataset_v1/
├── README.md
├── manifest.json
├── index.html
├── jsonl/
│   ├── nodes.jsonl
│   ├── edges.jsonl
│   ├── references.jsonl
│   ├── source_sentence_reviews.jsonl
│   ├── edge_reviews.jsonl
│   ├── node_packets.jsonl
│   ├── course_lessons.jsonl
│   ├── universe_nodes.jsonl
│   └── universe_edges.jsonl
└── parquet/                 # present when pyarrow is installed
    ├── nodes.parquet
    ├── edges.parquet
    ├── references.parquet
    ├── source_sentence_reviews.parquet
    ├── edge_reviews.parquet
    ├── node_packets.parquet
    ├── course_lessons.parquet
    ├── universe_nodes.parquet
    └── universe_edges.parquet
```

## Push to Hugging Face

Set the target dataset id and use an authenticated Hugging Face token. Use `PYTHON=python` if that interpreter has `pyarrow` and you want parquet included in the upload:

```bash
HF_DATASET_ID=PeytonT/ai_atlas PYTHON=python make hf-dataset-push
```

The exporter calls `huggingface_hub` with `repo_type="dataset"` and uploads the generated folder.

## Interactive Universe

`tools/build_universe.py` creates a deterministic 3D layout using the atlas layer order as the z-axis and a radial arrangement within each layer. The resulting JSONL files are intentionally close to the `/data/repository_library` universe exports:

| Repository Library | AI Atlas |
|---|---|
| `exports/_universe/nodes.jsonl` | `exports/universe/nodes.jsonl` |
| `exports/_universe/edges.jsonl` | `exports/universe/edges.jsonl` |
| `exports/_universe/manifest.json` | `exports/universe/manifest.json` |

`make universe` also writes `exports/universe/index.html`, a standalone interactive webpage with embedded universe data. A separate viewer can also consume `universe_nodes` and `universe_edges` directly from the Hugging Face parquet files or the local JSONL files.

## Design Rule

The dataset card and export metadata must keep the same scope statement as the repository: this is a bounded, source-audited dependency atlas, not a universal proof that all AI knowledge has been exhausted.

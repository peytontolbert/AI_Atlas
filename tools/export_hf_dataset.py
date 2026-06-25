#!/usr/bin/env python3
"""Export the AI Dependency Atlas as a Hugging Face-ready dataset."""
from __future__ import annotations

import argparse
import json
import hashlib
import os
import time
from pathlib import Path
from typing import Any, Iterable

DEFAULT_OUTPUT_DIR = Path("exports/huggingface/ai_atlas_dataset_v1")
DEFAULT_DATASET_ID = "PeytonT/ai_atlas"


def try_pyarrow():
    try:
        import pyarrow as pa  # type: ignore
        import pyarrow.parquet as pq  # type: ignore
    except ImportError:
        return None, None
    return pa, pq


def require_pyarrow():
    pa, pq = try_pyarrow()
    if pa is None or pq is None:
        raise RuntimeError("pyarrow is not installed for this Python interpreter")
    return pa, pq


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                row = json.loads(line)
                if isinstance(row, dict):
                    yield row


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return len(rows)


def write_parquet(path: Path, rows: list[dict[str, Any]], schema: Any) -> int:
    pa, pq = require_pyarrow()
    path.parent.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist(rows, schema=schema)
    pq.write_table(table, path, compression="zstd", use_dictionary=True)
    return table.num_rows


def layer_order() -> list[str]:
    return ["foundation", "representation", "paradigm", "objective", "mechanism", "model", "training", "memory", "reasoning", "alignment", "infrastructure", "system"]


def atlas_edges(atlas: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for node in atlas.get("nodes", []):
        node_id = str(node.get("id") or "")
        for dep in node.get("dependencies") or []:
            dependency_id = str(dep.get("id") or "")
            edge_key = f"{node_id}->{dependency_id}:{dep.get('type') or ''}"
            rows.append({
                "edge_id": hashlib.sha256(edge_key.encode("utf-8")).hexdigest()[:16],
                "node_id": node_id,
                "dependency_id": dependency_id,
                "type": str(dep.get("type") or ""),
                "strength": str(dep.get("strength") or ""),
                "rationale": str(dep.get("rationale") or ""),
            })
    return rows


def node_rows(atlas: dict[str, Any]) -> Iterable[dict[str, Any]]:
    downstream: dict[str, int] = {}
    for edge in atlas_edges(atlas):
        dep = str(edge.get("dependency_id") or "")
        if dep:
            downstream[dep] = downstream.get(dep, 0) + 1
    for node in atlas.get("nodes", []):
        node_id = str(node.get("id") or "")
        deps = node.get("dependencies") or []
        yield {
            "node_id": node_id,
            "label": str(node.get("label") or ""),
            "layer": str(node.get("layer") or ""),
            "tags": [str(x) for x in node.get("tags") or []],
            "aliases": [str(x) for x in node.get("aliases") or []],
            "definition": str(node.get("definition") or ""),
            "why_it_matters": str(node.get("why_it_matters") or ""),
            "examples": [str(x) for x in node.get("examples") or []],
            "limitations": [str(x) for x in node.get("limitations") or []],
            "maturity": str(node.get("maturity") or ""),
            "editorial_status": str(node.get("editorial_status") or ""),
            "terminal": bool(node.get("terminal")),
            "terminal_reason": str(node.get("terminal_reason") or ""),
            "reference_ids": [str(x) for x in node.get("reference_ids") or []],
            "dependency_count": len(deps),
            "downstream_count": downstream.get(node_id, 0),
            "node_json": compact_json(node),
        }


def edge_rows(atlas: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for edge in atlas_edges(atlas):
        yield {
            "edge_id": str(edge.get("edge_id") or ""),
            "node_id": str(edge.get("node_id") or ""),
            "dependency_id": str(edge.get("dependency_id") or ""),
            "type": str(edge.get("type") or ""),
            "strength": str(edge.get("strength") or ""),
            "rationale": str(edge.get("rationale") or ""),
            "edge_json": compact_json(edge),
        }


def reference_rows(atlas: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for ref in atlas.get("references", []):
        yield {"reference_id": str(ref.get("id") or ""), "title": str(ref.get("title") or ""), "url": str(ref.get("url") or ""), "reference_json": compact_json(ref)}


def packet_rows(root: Path) -> Iterable[dict[str, Any]]:
    for path in sorted((root / "audit" / "node_packets").glob("*.json")):
        if path.name == "index.json":
            continue
        packet = json.loads(path.read_text(encoding="utf-8"))
        yield {"node_id": str(packet.get("node_id") or path.stem), "label": str(packet.get("label") or ""), "layer": str(packet.get("layer") or ""), "editorial_status": str(packet.get("editorial_status") or ""), "packet_json": compact_json(packet)}


def sentence_review_rows(root: Path) -> Iterable[dict[str, Any]]:
    for row in iter_jsonl(root / "audit" / "source_sentence_ledger.jsonl"):
        yield {"unit_id": str(row.get("unit_id") or ""), "node_id": str(row.get("node_id") or ""), "field": str(row.get("field") or ""), "text": str(row.get("text") or ""), "source_ids": [str(x) for x in row.get("source_ids") or []], "evidence_location": str(row.get("evidence_location") or ""), "reviewer": str(row.get("reviewer") or ""), "review_date": str(row.get("review_date") or ""), "verdict": str(row.get("verdict") or ""), "notes": str(row.get("notes") or ""), "review_json": compact_json(row)}


def edge_review_rows(root: Path) -> Iterable[dict[str, Any]]:
    for row in iter_jsonl(root / "audit" / "edge_review_ledger.jsonl"):
        yield {"edge_id": str(row.get("edge_id") or ""), "node_id": str(row.get("node_id") or ""), "dependency_id": str(row.get("dependency_id") or ""), "source_ids": [str(x) for x in row.get("source_ids") or []], "evidence_location": str(row.get("evidence_location") or ""), "reviewer": str(row.get("reviewer") or ""), "review_date": str(row.get("review_date") or ""), "verdict": str(row.get("verdict") or ""), "notes": str(row.get("notes") or ""), "review_json": compact_json(row)}


def lesson_rows(root: Path) -> Iterable[dict[str, Any]]:
    paths = sorted((root / "course").glob("*.md")) + sorted((root / "course" / "lessons").glob("*.md"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("#")), path.stem)
        yield {"path": rel, "title": title, "section": "lesson" if "/lessons/" in rel else "course", "text": text}


def universe_node_rows(root: Path, atlas: dict[str, Any]) -> Iterable[dict[str, Any]]:
    path = root / "exports" / "universe" / "nodes.jsonl"
    if path.is_file():
        yield from iter_jsonl(path)
        return
    layer_index = {layer: i for i, layer in enumerate(layer_order())}
    for node in atlas.get("nodes", []):
        yield {"node_id": str(node.get("id") or ""), "label": str(node.get("label") or ""), "layer": str(node.get("layer") or ""), "kind": "concept", "x": float(layer_index.get(str(node.get("layer") or ""), 0)), "y": float(len(node.get("dependencies") or [])), "z": 0.0, "size": float(1 + len(node.get("dependencies") or [])), "color": str(node.get("layer") or ""), "node_json": compact_json(node)}


def universe_edge_rows(root: Path, atlas: dict[str, Any]) -> Iterable[dict[str, Any]]:
    path = root / "exports" / "universe" / "edges.jsonl"
    if path.is_file():
        yield from iter_jsonl(path)
        return
    for edge in atlas_edges(atlas):
        yield {"src": str(edge.get("node_id") or ""), "dst": str(edge.get("dependency_id") or ""), "type": str(edge.get("type") or ""), "weight": 1.0 if edge.get("strength") == "core" else 0.6 if edge.get("strength") == "common" else 0.3, "edge_json": compact_json(edge)}


def schemas() -> dict[str, Any]:
    pa, _ = require_pyarrow()
    return {
        "nodes": pa.schema([("node_id", pa.string()), ("label", pa.string()), ("layer", pa.string()), ("tags", pa.list_(pa.string())), ("aliases", pa.list_(pa.string())), ("definition", pa.string()), ("why_it_matters", pa.string()), ("examples", pa.list_(pa.string())), ("limitations", pa.list_(pa.string())), ("maturity", pa.string()), ("editorial_status", pa.string()), ("terminal", pa.bool_()), ("terminal_reason", pa.string()), ("reference_ids", pa.list_(pa.string())), ("dependency_count", pa.int32()), ("downstream_count", pa.int32()), ("node_json", pa.string())]),
        "edges": pa.schema([("edge_id", pa.string()), ("node_id", pa.string()), ("dependency_id", pa.string()), ("type", pa.string()), ("strength", pa.string()), ("rationale", pa.string()), ("edge_json", pa.string())]),
        "references": pa.schema([("reference_id", pa.string()), ("title", pa.string()), ("url", pa.string()), ("reference_json", pa.string())]),
        "source_sentence_reviews": pa.schema([("unit_id", pa.string()), ("node_id", pa.string()), ("field", pa.string()), ("text", pa.string()), ("source_ids", pa.list_(pa.string())), ("evidence_location", pa.string()), ("reviewer", pa.string()), ("review_date", pa.string()), ("verdict", pa.string()), ("notes", pa.string()), ("review_json", pa.string())]),
        "edge_reviews": pa.schema([("edge_id", pa.string()), ("node_id", pa.string()), ("dependency_id", pa.string()), ("source_ids", pa.list_(pa.string())), ("evidence_location", pa.string()), ("reviewer", pa.string()), ("review_date", pa.string()), ("verdict", pa.string()), ("notes", pa.string()), ("review_json", pa.string())]),
        "node_packets": pa.schema([("node_id", pa.string()), ("label", pa.string()), ("layer", pa.string()), ("editorial_status", pa.string()), ("packet_json", pa.string())]),
        "course_lessons": pa.schema([("path", pa.string()), ("title", pa.string()), ("section", pa.string()), ("text", pa.string())]),
        "universe_nodes": pa.schema([("node_id", pa.string()), ("label", pa.string()), ("layer", pa.string()), ("kind", pa.string()), ("x", pa.float32()), ("y", pa.float32()), ("z", pa.float32()), ("size", pa.float32()), ("color", pa.string()), ("node_json", pa.string())]),
        "universe_edges": pa.schema([("src", pa.string()), ("dst", pa.string()), ("type", pa.string()), ("weight", pa.float32()), ("edge_json", pa.string())]),
    }


def dataset_card(dataset_id: str, manifest: dict[str, Any]) -> str:
    configs = "\n".join(f"- `{name}`: {rows:,} rows" for name, rows in manifest["configs"].items())
    yaml_configs = "\n".join(f"- config_name: {name}" for name in manifest["configs"])
    return f"""---
license: mit
task_categories:
- text-retrieval
- graph-ml
- question-answering
language:
- en
pretty_name: AI Dependency Atlas
size_categories:
- n<10K
configs:
{yaml_configs}
---

# AI Dependency Atlas

This dataset packages the AI Dependency Atlas as one Hugging Face dataset with multiple configs for graph, audit, source-review, and teaching-course use. It always includes JSONL data files and includes parquet files when pyarrow is available during export.

Dataset id target: `{dataset_id}`

## Configs

{configs}

## Scope

The atlas is a bounded, source-audited dependency map of AI concept families. It does not claim to enumerate every paper, model release, dataset, benchmark, product, or future term.

## Provenance

- Canonical source: `data/atlas.json`
- Source audit: `audit/source_sentence_ledger.jsonl` and `audit/edge_review_ledger.jsonl`
- Build time: {manifest['built_at']}
"""


def export(root: Path, output_dir: Path, dataset_id: str) -> dict[str, Any]:
    atlas = json.loads((root / "data" / "atlas.json").read_text(encoding="utf-8"))
    parquet_dir = output_dir / "parquet"
    jsonl_dir = output_dir / "jsonl"
    row_factories = {
        "nodes": lambda: list(node_rows(atlas)),
        "edges": lambda: list(edge_rows(atlas)),
        "references": lambda: list(reference_rows(atlas)),
        "source_sentence_reviews": lambda: list(sentence_review_rows(root)),
        "edge_reviews": lambda: list(edge_review_rows(root)),
        "node_packets": lambda: list(packet_rows(root)),
        "course_lessons": lambda: list(lesson_rows(root)),
        "universe_nodes": lambda: list(universe_node_rows(root, atlas)),
        "universe_edges": lambda: list(universe_edge_rows(root, atlas)),
    }
    pa, _ = try_pyarrow()
    schema_map = schemas() if pa is not None else {}
    counts: dict[str, int] = {}
    formats = ["jsonl"]
    for name, factory in row_factories.items():
        rows = factory()
        counts[name] = write_jsonl(jsonl_dir / f"{name}.jsonl", rows)
        if pa is not None:
            write_parquet(parquet_dir / f"{name}.parquet", rows, schema_map[name])
    if pa is not None:
        formats.append("parquet")
    manifest = {"dataset_id": dataset_id, "built_at": int(time.time()), "source": "data/atlas.json", "configs": counts, "formats": formats, "jsonl_dir": str(jsonl_dir), "parquet_dir": str(parquet_dir) if pa is not None else ""}
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "README.md").write_text(dataset_card(dataset_id, manifest), encoding="utf-8")
    return manifest


def push_to_hub(output_dir: Path, dataset_id: str, private: bool) -> None:
    try:
        from huggingface_hub import HfApi  # type: ignore
    except ImportError as exc:
        raise SystemExit("huggingface_hub is required to push. Install with: python -m pip install huggingface_hub") from exc
    api = HfApi()
    api.create_repo(repo_id=dataset_id, repo_type="dataset", private=private, exist_ok=True)
    api.upload_folder(repo_id=dataset_id, repo_type="dataset", folder_path=str(output_dir))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--dataset-id", default=os.environ.get("HF_DATASET_ID", DEFAULT_DATASET_ID))
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--private", action="store_true")
    args = parser.parse_args()
    manifest = export(args.root.resolve(), args.output_dir, args.dataset_id)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    if args.push:
        push_to_hub(args.output_dir, args.dataset_id, args.private)
        print(f"Pushed dataset to https://huggingface.co/datasets/{args.dataset_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

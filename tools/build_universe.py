#!/usr/bin/env python3
"""Build layout-ready universe artifacts for the AI Dependency Atlas."""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

LAYER_ORDER = ["foundation", "representation", "paradigm", "objective", "mechanism", "model", "training", "memory", "reasoning", "alignment", "infrastructure", "system"]
LAYER_COLORS = {"foundation": "#456990", "representation": "#49a078", "paradigm": "#f4a261", "objective": "#e76f51", "mechanism": "#2a9d8f", "model": "#7b2cbf", "training": "#bc6c25", "memory": "#118ab2", "reasoning": "#ef476f", "alignment": "#06d6a0", "infrastructure": "#8d99ae", "system": "#ffb703"}


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def build(root: Path, output_dir: Path) -> dict[str, Any]:
    atlas = json.loads((root / "data" / "atlas.json").read_text(encoding="utf-8"))
    nodes = atlas.get("nodes", [])
    edges = []
    for node in nodes:
        node_id = str(node.get("id") or "")
        for dep in node.get("dependencies") or []:
            edges.append({"node_id": node_id, "dependency_id": str(dep.get("id") or ""), "type": str(dep.get("type") or ""), "strength": str(dep.get("strength") or ""), "rationale": str(dep.get("rationale") or "")})
    layer_index = {layer: idx for idx, layer in enumerate(LAYER_ORDER)}
    layer_counts = {layer: 0 for layer in LAYER_ORDER}
    layer_totals = {layer: sum(1 for n in nodes if n.get("layer") == layer) for layer in LAYER_ORDER}
    downstream: dict[str, int] = {}
    for edge in edges:
        dep = str(edge.get("dependency_id") or "")
        if dep:
            downstream[dep] = downstream.get(dep, 0) + 1
    universe_nodes: list[dict[str, Any]] = []
    for node in nodes:
        layer = str(node.get("layer") or "")
        idx = layer_counts.get(layer, 0)
        layer_counts[layer] = idx + 1
        total = max(1, layer_totals.get(layer, 1))
        angle = (2.0 * math.pi * idx) / total
        radius = 8.0 + layer_index.get(layer, 0) * 3.5
        dep_count = len(node.get("dependencies") or [])
        down_count = downstream.get(str(node.get("id") or ""), 0)
        universe_nodes.append({"node_id": str(node.get("id") or ""), "label": str(node.get("label") or ""), "layer": layer, "kind": "concept", "x": round(math.cos(angle) * radius, 6), "y": round(math.sin(angle) * radius, 6), "z": round((layer_index.get(layer, 0) - 5.5) * 2.0, 6), "size": float(3 + min(10, dep_count + down_count)), "color": LAYER_COLORS.get(layer, "#cccccc"), "node_json": compact_json(node)})
    universe_edges = [{"src": str(edge.get("node_id") or ""), "dst": str(edge.get("dependency_id") or ""), "type": str(edge.get("type") or ""), "weight": 1.0 if edge.get("strength") == "core" else 0.6 if edge.get("strength") == "common" else 0.3, "edge_json": compact_json(edge)} for edge in edges]
    write_jsonl(output_dir / "nodes.jsonl", universe_nodes)
    write_jsonl(output_dir / "edges.jsonl", universe_edges)
    manifest = {"built_at": int(time.time()), "node_count": len(universe_nodes), "edge_count": len(universe_edges), "layers": LAYER_ORDER, "nodes_path": "nodes.jsonl", "edges_path": "edges.jsonl"}
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, default=Path("exports/universe"))
    args = parser.parse_args()
    print(json.dumps(build(args.root.resolve(), args.output_dir), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

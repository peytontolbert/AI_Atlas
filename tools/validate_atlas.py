#!/usr/bin/env python3
"""Validate the canonical AI Dependency Atlas data and emit machine-readable reports."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

EDGE_TYPES = {
    "requires", "uses", "represents_with", "optimizes_for", "trained_under",
    "specializes", "composes", "adapts", "retrieves_from", "searches_with",
    "verifies_with", "evaluates_or_constrains", "operationalizes", "applies",
}
FORBIDDEN_PHRASES = [
    "An architecture family that combines representations",
    "A pipeline technique used to train",
    "A mechanism for storing, retrieving",
    "A method for deliberate inference",
    "A method for measuring, interpreting",
    "An operational component used to train",
    "An end-to-end intelligent system assembled",
]
REQUIRED_MODERN_COVERAGE = {
    "empirical_scaling_laws", "compute_optimal_training", "grpo", "rlvr",
    "test_time_compute", "tree_of_thoughts", "graph_of_thoughts",
    "neural_architecture_search", "output_watermarking", "content_provenance",
    "sim_to_real_transfer", "domain_randomization", "mixture_of_depths",
    "structured_outputs", "grammar_constrained_decoding", "formal_model_verification",
    "formal_agent_verification", "encoder_only_transformer",
}


def norm(text: str) -> str:
    return re.sub(r"\W+", " ", text.lower()).strip()


def validate(data_path: Path, schema_path: Path) -> dict:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, dict] = {}

    schema_errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data),
        key=lambda error: list(error.path),
    )
    if schema_errors:
        for error in schema_errors:
            path = ".".join(str(x) for x in error.path) or "$"
            errors.append(f"schema:{path}: {error.message}")
    checks["json_schema"] = {"passed": not schema_errors, "issues": len(schema_errors)}

    layers = data.get("layers", [])
    nodes = data.get("nodes", [])
    refs = data.get("references", [])
    layer_ids = [layer.get("id") for layer in layers]
    layer_orders = [layer.get("order") for layer in layers]
    node_ids = [node.get("id") for node in nodes]
    ref_ids = [ref.get("id") for ref in refs]

    def duplicate_values(values):
        return sorted(value for value, count in Counter(values).items() if count > 1)

    duplicate_layers = duplicate_values(layer_ids)
    duplicate_orders = duplicate_values(layer_orders)
    duplicate_nodes = duplicate_values(node_ids)
    duplicate_refs = duplicate_values(ref_ids)
    for name, values in [
        ("layer IDs", duplicate_layers), ("layer orders", duplicate_orders),
        ("node IDs", duplicate_nodes), ("reference IDs", duplicate_refs),
    ]:
        if values:
            errors.append(f"duplicate {name}: {values}")
    checks["unique_identifiers"] = {
        "passed": not any([duplicate_layers, duplicate_orders, duplicate_nodes, duplicate_refs]),
        "issues": sum(map(len, [duplicate_layers, duplicate_orders, duplicate_nodes, duplicate_refs])),
    }

    node_by_id = {node["id"]: node for node in nodes if "id" in node}
    ref_set = set(ref_ids)
    layer_order = {layer["id"]: layer["order"] for layer in layers if "id" in layer and "order" in layer}

    missing_layers = [node["id"] for node in nodes if node.get("layer") not in layer_order]
    if missing_layers:
        errors.append(f"nodes with unknown layers: {missing_layers}")
    checks["layer_membership"] = {"passed": not missing_layers, "issues": len(missing_layers)}

    missing_deps: list[str] = []
    self_edges: list[str] = []
    duplicate_edges: list[str] = []
    upward_edges: list[str] = []
    bad_edge_types: list[str] = []
    missing_refs: list[str] = []
    consumers: dict[str, list[str]] = defaultdict(list)
    edge_count = 0
    same_layer_edges = 0
    relation_counts: Counter[str] = Counter()
    strength_counts: Counter[str] = Counter()

    for node in nodes:
        seen = set()
        for edge in node.get("dependencies", []):
            edge_count += 1
            dep_id = edge.get("id")
            if dep_id in seen:
                duplicate_edges.append(f"{node['id']}->{dep_id}")
            seen.add(dep_id)
            if dep_id == node.get("id"):
                self_edges.append(node["id"])
            if dep_id not in node_by_id:
                missing_deps.append(f"{node['id']}->{dep_id}")
                continue
            consumers[dep_id].append(node["id"])
            dep = node_by_id[dep_id]
            if layer_order.get(dep["layer"], -1) > layer_order.get(node["layer"], -1):
                upward_edges.append(f"{node['id']}({node['layer']})->{dep_id}({dep['layer']})")
            if dep["layer"] == node["layer"]:
                same_layer_edges += 1
            relation_counts[edge.get("type")] += 1
            strength_counts[edge.get("strength")] += 1
            if edge.get("type") not in EDGE_TYPES:
                bad_edge_types.append(f"{node['id']}->{dep_id}:{edge.get('type')}")
        for ref_id in node.get("reference_ids", []):
            if ref_id not in ref_set:
                missing_refs.append(f"{node['id']}->{ref_id}")

    for label, values in [
        ("missing dependencies", missing_deps), ("self edges", self_edges),
        ("duplicate dependency edges", duplicate_edges), ("upward layer edges", upward_edges),
        ("unknown edge types", bad_edge_types), ("missing references", missing_refs),
    ]:
        if values:
            errors.append(f"{label}: {values[:30]}" + (" …" if len(values) > 30 else ""))
    checks["edge_integrity"] = {
        "passed": not any([missing_deps, self_edges, duplicate_edges, upward_edges, bad_edge_types]),
        "issues": sum(map(len, [missing_deps, self_edges, duplicate_edges, upward_edges, bad_edge_types])),
        "same_layer_edges": same_layer_edges,
    }
    checks["reference_integrity"] = {"passed": not missing_refs, "issues": len(missing_refs)}

    # Directed acyclic graph check and maximum dependency depth.
    indegree = {node_id: 0 for node_id in node_by_id}
    adjacency: dict[str, list[str]] = defaultdict(list)
    for node in nodes:
        for edge in node.get("dependencies", []):
            if edge["id"] in node_by_id:
                adjacency[edge["id"]].append(node["id"])
                indegree[node["id"]] += 1
    queue = deque(sorted(node_id for node_id, degree in indegree.items() if degree == 0))
    topological: list[str] = []
    while queue:
        current = queue.popleft()
        topological.append(current)
        for child in adjacency[current]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    cyclic = sorted(node_id for node_id, degree in indegree.items() if degree > 0)
    if cyclic:
        errors.append(f"cycle detected among: {cyclic[:40]}")
    depth = {node_id: 0 for node_id in node_by_id}
    if not cyclic:
        for current in topological:
            for child in adjacency[current]:
                depth[child] = max(depth[child], depth[current] + 1)
    max_depth = max(depth.values(), default=0)
    checks["acyclic_graph"] = {"passed": not cyclic, "issues": len(cyclic), "max_depth": max_depth}

    # Rich-content and anti-boilerplate checks.
    definitions = [norm(node.get("definition", "")) for node in nodes]
    duplicate_definitions = duplicate_values(definitions)
    boilerplate = [
        node["id"] for node in nodes
        if any(phrase.lower() in node.get("definition", "").lower() for phrase in FORBIDDEN_PHRASES)
    ]
    incomplete_content = []
    for node in nodes:
        if len(node.get("definition", "")) < 65:
            incomplete_content.append(f"{node['id']}:definition")
        if len(node.get("why_it_matters", "")) < 45:
            incomplete_content.append(f"{node['id']}:why_it_matters")
        if len(node.get("examples", [])) < 2:
            incomplete_content.append(f"{node['id']}:examples")
        if len(node.get("limitations", [])) < 1:
            incomplete_content.append(f"{node['id']}:limitations")
        if len(node.get("reference_ids", [])) < 1:
            incomplete_content.append(f"{node['id']}:reference_ids")
    if duplicate_definitions:
        errors.append(f"duplicate normalized definitions: {duplicate_definitions[:10]}")
    if boilerplate:
        errors.append(f"forbidden boilerplate definitions: {boilerplate}")
    if incomplete_content:
        errors.append(f"incomplete node content: {incomplete_content[:40]}")
    checks["rich_content"] = {
        "passed": not any([duplicate_definitions, boilerplate, incomplete_content]),
        "unique_definitions": len(nodes) - len(duplicate_definitions),
        "boilerplate_definitions": len(boilerplate),
        "incomplete_fields": len(incomplete_content),
    }

    # Terminal declarations must agree with actual graph consumers.
    terminal_mismatches = []
    non_system_terminals = []
    for node in nodes:
        actual_terminal = len(consumers.get(node["id"], [])) == 0
        if node.get("terminal") != actual_terminal:
            terminal_mismatches.append(node["id"])
        if actual_terminal and not node.get("terminal_reason"):
            terminal_mismatches.append(f"{node['id']}:missing_reason")
        if actual_terminal and node.get("layer") != "system":
            non_system_terminals.append(node["id"])
    if terminal_mismatches:
        errors.append(f"terminal declaration mismatches: {terminal_mismatches}")
    if non_system_terminals:
        warnings.append(f"non-system terminal concepts: {non_system_terminals}")
    checks["terminal_semantics"] = {
        "passed": not terminal_mismatches,
        "issues": len(terminal_mismatches),
        "terminal_nodes": sum(1 for node in nodes if node.get("terminal")),
        "non_system_terminal_nodes": len(non_system_terminals),
    }

    # Declared scope coverage.
    missing_modern = sorted(REQUIRED_MODERN_COVERAGE - set(node_by_id))
    if missing_modern:
        errors.append(f"missing declared modern coverage nodes: {missing_modern}")
    checks["declared_modern_coverage"] = {
        "passed": not missing_modern,
        "present": len(REQUIRED_MODERN_COVERAGE) - len(missing_modern),
        "required": len(REQUIRED_MODERN_COVERAGE),
    }

    # Statistics must be reproducible from source data.
    layer_counts = Counter(node["layer"] for node in nodes)
    referenced_ids = {ref_id for node in nodes for ref_id in node.get("reference_ids", [])}
    unused_refs = sorted(ref_set - referenced_ids)
    if unused_refs:
        warnings.append(f"unused references: {unused_refs}")
    actual_stats = {
        "nodes": len(nodes),
        "typed_edges": edge_count,
        "references": len(refs),
        "layers": len(layers),
        "unique_definitions": len(nodes) - len(duplicate_definitions),
        "boilerplate_definitions": len(boilerplate),
        "max_dependency_depth": max_depth,
        "terminal_nodes": sum(1 for node in nodes if node.get("terminal")),
        "non_system_terminal_nodes": len(non_system_terminals),
        "curated_nodes": sum(node.get("editorial_status") == "curated" for node in nodes),
        "graph_derived_context_nodes": sum(node.get("editorial_status") == "definition_curated_context_graph_derived" for node in nodes),
        "layer_counts": dict(layer_counts),
        "relation_counts": dict(relation_counts),
    }
    declared_stats = data.get("meta", {}).get("stats", {})
    mismatched_stats = {
        key: {"declared": declared_stats.get(key), "actual": value}
        for key, value in actual_stats.items()
        if declared_stats.get(key) != value
    }
    if mismatched_stats:
        errors.append(f"metadata stats mismatch: {mismatched_stats}")
    checks["reproducible_statistics"] = {
        "passed": not mismatched_stats,
        "issues": len(mismatched_stats),
    }

    report = {
        "passed": not errors,
        "data_file": str(data_path),
        "schema_file": str(schema_path),
        "summary": {
            **actual_stats,
            "same_layer_edges": same_layer_edges,
            "referenced_nodes": sum(1 for node in nodes if node.get("reference_ids")),
            "typed_edge_coverage_percent": round(100.0 * sum(len(node.get("dependencies", [])) for node in nodes) / max(edge_count, 1), 2),
            "rich_node_coverage_percent": round(100.0 * (len(nodes) - len(incomplete_content)) / max(len(nodes), 1), 2),
            "reference_coverage_percent": round(100.0 * sum(bool(node.get("reference_ids")) for node in nodes) / max(len(nodes), 1), 2),
            "unused_references": len(unused_refs),
            "strength_counts": dict(strength_counts),
        },
        "checks": checks,
        "errors": errors,
        "warnings": warnings,
    }
    return report


def markdown_report(report: dict) -> str:
    icon = "PASS" if report["passed"] else "FAIL"
    s = report["summary"]
    lines = [
        "# AI Dependency Atlas Validation Report",
        "",
        f"**Overall: {icon}**",
        "",
        "## Recomputed metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Nodes | {s['nodes']} |",
        f"| Typed edges | {s['typed_edges']} |",
        f"| References | {s['references']} |",
        f"| Layers | {s['layers']} |",
        f"| Unique definitions | {s['unique_definitions']} |",
        f"| Boilerplate definitions | {s['boilerplate_definitions']} |",
        f"| Reference coverage | {s['reference_coverage_percent']}% |",
        f"| Rich-node coverage | {s['rich_node_coverage_percent']}% |",
        f"| Non-system terminal nodes | {s['non_system_terminal_nodes']} |",
        f"| Manually curated supporting context | {s['curated_nodes']} |",
        f"| Graph-derived supporting context | {s['graph_derived_context_nodes']} |",
        f"| Maximum dependency depth | {s['max_dependency_depth']} |",
        f"| Same-layer edges | {s['same_layer_edges']} |",
        "",
        "## Checks",
        "",
        "| Check | Result | Details |",
        "|---|---|---|",
    ]
    for name, item in report["checks"].items():
        details = ", ".join(f"{k}={v}" for k, v in item.items() if k != "passed")
        lines.append(f"| `{name}` | {'PASS' if item['passed'] else 'FAIL'} | {details} |")
    if report["errors"]:
        lines += ["", "## Errors", ""] + [f"- {error}" for error in report["errors"]]
    if report["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {warning}" for warning in report["warnings"]]
    return "\n".join(lines) + "\n"


def main() -> int:
    here = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=here / "data" / "atlas.json")
    parser.add_argument("--schema", type=Path, default=here / "schema" / "atlas.schema.json")
    parser.add_argument("--json-report", type=Path, default=here / "dist" / "validation_report.json")
    parser.add_argument("--md-report", type=Path, default=here / "dist" / "validation_report.md")
    args = parser.parse_args()

    report = validate(args.data, args.schema)
    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.md_report.write_text(markdown_report(report), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    if report["errors"]:
        print("Validation failed:", file=sys.stderr)
        for error in report["errors"]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

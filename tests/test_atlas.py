from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import unittest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "atlas.json"
SCHEMA_PATH = ROOT / "schema" / "atlas.schema.json"
HTML_PATH = ROOT / "dist" / "ai_dependency_atlas_v2.html"
MANIFEST_PATH = ROOT / "dist" / "build_manifest.json"
VALIDATOR_PATH = ROOT / "tools" / "validate_atlas.py"


def import_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class AtlasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "build_atlas.py")],
            check=True,
            cwd=ROOT,
        )
        cls.data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        cls.nodes = {node["id"]: node for node in cls.data["nodes"]}

    def test_validator_passes_without_warnings(self) -> None:
        validator = import_module("atlas_validator_test", VALIDATOR_PATH)
        report = validator.validate(DATA_PATH, SCHEMA_PATH)
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(report["warnings"], [])

    def test_declared_scope_is_explicitly_non_exhaustive(self) -> None:
        meta = self.data["meta"]
        joined = " ".join(
            [meta["status"], meta["scope_statement"], *meta["known_exclusions"]]
        ).lower()
        self.assertIn("not exhaustive", joined)
        self.assertIn("family-level", joined)
        self.assertIn("named model", joined)

    def test_modern_and_missing_v1_topics_are_present(self) -> None:
        required = {
            "empirical_scaling_laws",
            "compute_optimal_training",
            "grpo",
            "rlvr",
            "test_time_compute",
            "tree_of_thoughts",
            "graph_of_thoughts",
            "neural_architecture_search",
            "output_watermarking",
            "content_provenance",
            "sim_to_real_transfer",
            "domain_randomization",
            "mixture_of_depths",
            "structured_outputs",
            "grammar_constrained_decoding",
            "formal_model_verification",
            "formal_agent_verification",
            "encoder_only_transformer",
        }
        self.assertEqual(required - set(self.nodes), set())

    def test_every_node_has_rich_validated_content(self) -> None:
        normalized = []
        editorial = Counter()
        for node in self.nodes.values():
            self.assertGreaterEqual(len(node["definition"]), 65)
            self.assertGreaterEqual(len(node["why_it_matters"]), 45)
            self.assertGreaterEqual(len(node["examples"]), 2)
            self.assertGreaterEqual(len(node["limitations"]), 1)
            self.assertGreaterEqual(len(node["reference_ids"]), 1)
            self.assertIn(
                node["editorial_status"],
                {"curated", "definition_curated_context_graph_derived"},
            )
            editorial[node["editorial_status"]] += 1
            normalized.append(re.sub(r"\W+", " ", node["definition"].lower()).strip())
        self.assertEqual(len(normalized), len(set(normalized)))
        self.assertEqual(editorial["curated"], self.data["meta"]["stats"]["curated_nodes"])
        self.assertEqual(
            editorial["definition_curated_context_graph_derived"],
            self.data["meta"]["stats"]["graph_derived_context_nodes"],
        )

    def test_every_edge_is_typed_and_justified(self) -> None:
        allowed_types = {
            "requires", "uses", "represents_with", "optimizes_for",
            "trained_under", "specializes", "composes", "adapts",
            "retrieves_from", "searches_with", "verifies_with",
            "evaluates_or_constrains", "operationalizes", "applies",
        }
        for node in self.nodes.values():
            targets = []
            for edge in node["dependencies"]:
                self.assertIn(edge["id"], self.nodes)
                self.assertIn(edge["type"], allowed_types)
                self.assertIn(edge["strength"], {"core", "common", "optional"})
                self.assertGreaterEqual(len(edge["rationale"]), 35)
                targets.append(edge["id"])
            self.assertEqual(len(targets), len(set(targets)))

    def test_reusable_nodes_have_downstream_consumers(self) -> None:
        consumers: dict[str, list[str]] = defaultdict(list)
        for node in self.nodes.values():
            for edge in node["dependencies"]:
                consumers[edge["id"]].append(node["id"])
        for node in self.nodes.values():
            if node["layer"] != "system":
                self.assertGreater(
                    len(consumers[node["id"]]),
                    0,
                    f"Reusable node has no declared consumer: {node['id']}",
                )

    def test_generated_html_is_standalone_and_embeds_canonical_data(self) -> None:
        html = HTML_PATH.read_text(encoding="utf-8")
        self.assertNotIn("__ATLAS_JSON__", html)
        self.assertNotRegex(html, r"<script\b[^>]*\bsrc=")
        self.assertNotRegex(html, r"<link\b[^>]*\brel=[\"']stylesheet[\"'][^>]*\bhref=")
        match = re.search(
            r'<script id="atlas-data" type="application/json">(.*?)</script>',
            html,
            flags=re.DOTALL,
        )
        self.assertIsNotNone(match)
        embedded = json.loads(match.group(1))
        self.assertEqual(embedded, self.data)

    def test_build_manifest_hashes_match(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        for filename, expected in manifest["generated_files"].items():
            self.assertEqual(digest(ROOT / "dist" / filename), expected)
        for relative, expected in manifest["inputs"].items():
            self.assertEqual(digest(ROOT / relative), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

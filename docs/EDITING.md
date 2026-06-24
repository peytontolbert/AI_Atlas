# Editing and Contribution Guide

## Source of truth

Edit only `data/atlas.json`. Do not manually modify generated files in `dist/`; the next build will replace them.

After every change:

```bash
make test
```

## Node schema

A node must include all fields below:

```json
{
  "id": "graph_rag",
  "label": "Graph RAG & structured retrieval",
  "layer": "memory",
  "tags": ["memory", "retrieval", "graphs"],
  "aliases": ["GraphRAG"],
  "definition": "Graph RAG retrieves entities, relations, communities, and multi-hop paths from an explicit graph before grounding generation or synthesis.",
  "why_it_matters": "It makes relational structure, entity identity, and multi-hop evidence available to downstream generation rather than reducing all knowledge to independent text chunks.",
  "examples": [
    "enterprise entity graphs",
    "scientific literature synthesis",
    "multi-hop question answering"
  ],
  "limitations": [
    "Graph construction, entity resolution, freshness, retrieval planning, and provenance can dominate system quality and operating cost."
  ],
  "editorial_status": "curated",
  "maturity": "established",
  "terminal": false,
  "terminal_reason": null,
  "reference_ids": ["ref_rag"],
  "dependencies": [
    {
      "id": "rag",
      "type": "retrieves_from",
      "strength": "core",
      "rationale": "Graph RAG specializes retrieval-augmented generation by replacing or augmenting flat document retrieval with structured relational retrieval."
    },
    {
      "id": "knowledge_graphs",
      "type": "retrieves_from",
      "strength": "core",
      "rationale": "Entities and typed relations provide the graph substrate traversed during structured retrieval."
    }
  ]
}
```

## Editorial status

Use exactly one value:

- `curated`: all supporting prose was manually authored and reviewed.
- `definition_curated_context_graph_derived`: the definition is concept-specific, while supporting role/example/limitation fields are generated from graph structure.

Do not mark a node `curated` merely because its text is grammatical. The distinction is provenance, not a quality score.

## Dependency direction

Store prerequisites on the higher-level node:

```text
system -> model -> mechanism -> foundation
```

Do not add a reverse edge to express “enables.” The viewer computes consumers automatically.

## Relationship types

Choose the narrowest correct relationship:

| Type | Use when the node… |
|---|---|
| `requires` | depends on a formal or computational substrate |
| `uses` | incorporates a reusable ingredient |
| `represents_with` | consumes or organizes a representation |
| `optimizes_for` | is selected through an objective |
| `trained_under` | follows a learning paradigm |
| `specializes` | narrows or extends an architecture family |
| `composes` | is assembled from a mechanism or model component |
| `adapts` | changes or combines model parameters |
| `retrieves_from` | obtains or stores information through the dependency |
| `searches_with` | explores alternatives through the dependency |
| `verifies_with` | checks candidate behavior through the dependency |
| `evaluates_or_constrains` | measures, governs, or limits behavior |
| `operationalizes` | makes the dependency deployable or scalable |
| `applies` | integrates the dependency into an end system |

Strength values:

- `core`: part of the canonical definition or necessary substrate;
- `common`: widely used but not logically required;
- `optional`: a supported integration or important modern variant.

## Adding references

Reference IDs are global and must match `^[a-z][a-z0-9_]*$`.

Prefer sources in this order:

1. original primary paper or specification;
2. authoritative standard or official technical report;
3. high-quality survey;
4. foundational textbook for broad concepts.

A node must have at least one reference pointer. Add node-specific references when practical; do not multiply low-value citations solely to raise a count.

## Terminal semantics

`terminal` is derived from graph topology:

- `true` means no node currently declares the concept as a dependency;
- every terminal node must have a `terminal_reason`;
- reusable non-system concepts should normally have at least one consumer;
- system leaves are expected terminal nodes.

The validator fails when the declaration disagrees with topology.

## Quality checklist for a new node

Before submission, verify:

- the concept is not merely a named model, product, library, benchmark, or dataset;
- the definition distinguishes it from its nearest neighbors;
- the node has at least two meaningful prerequisites unless it is a foundation root;
- each edge type, strength, and rationale is defensible;
- at least one downstream consumer exists for reusable concepts;
- examples are actual methods, systems, or usage settings—not synonyms;
- limitations describe failure conditions or tradeoffs rather than generic uncertainty;
- references are relevant to the node;
- maturity is defensible;
- `make test` passes.

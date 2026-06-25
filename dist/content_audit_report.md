# AI Dependency Atlas Content Audit

> This audit measures structural integrity, field coverage, and editorial provenance. It does not certify universal research completeness, historical priority, or the truth of every dependency judgment.

## Structural and editorial summary

| Measure | Value |
|---|---:|
| Nodes | 320 |
| Typed edges | 1225 |
| Reference records | 63 |
| Unique normalized definitions | 320 |
| Manually curated supporting context | 42 |
| Definition-curated, graph-derived supporting context | 278 |
| Non-system nodes without consumers | 0 |

## Editorial disclosure

All concept definitions are concept-specific and unique under normalization. The `editorial_status` field makes a second distinction: supporting sections for some nodes were manually written, while others were generated from validated dependency and consumer relationships. Graph-derived supporting context is useful for navigation, but it is not represented as equivalent to a full textbook treatment.

| Pattern | Count |
|---|---:|
| Role summaries beginning with `The role of …` | 257 |
| Nodes containing a `substrate for …` example | 257 |
| Nodes using graph-derived baseline context | 278 |

## Field-length distribution

| Field | Minimum | Median | Mean | Maximum |
|---|---:|---:|---:|---:|
| definition | 72 | 143.5 | 133.23 | 188 |
| why it matters | 79 | 231.0 | 220.04 | 348 |
| edge rationale | 74 | 128 | 128.8 | 189 |

## Reference usage

- Nodes with at least one reference pointer: **320 / 320**
- Nodes with multiple reference pointers: **31 / 320**
- A reference pointer is evidence of a relevant source family; it is not a claim that every sentence has been individually source-verified.

| Most reused reference | Nodes |
|---|---:|
| Artificial Intelligence: A Modern Approach, 4th ed. | 100 |
| Deep Learning | 77 |
| Probabilistic Machine Learning: An Introduction | 37 |
| AI Risk Management Framework 1.0 | 18 |
| Designing Data-Intensive Applications | 13 |
| Attention Is All You Need | 7 |
| Formal Methods for Machine Learning: A Survey | 5 |
| A Survey of Structured Output Generation from LLMs | 5 |
| Reinforcement Learning with Verifiable Rewards: A Survey | 4 |
| Training Compute-Optimal Large Language Models | 3 |

## Interpretation

The atlas is structurally complete against its declared family-level scope and passes its machine checks. Editorial depth is intentionally disclosed rather than hidden: the next improvement frontier is manual refinement of graph-derived role summaries, examples, limitations, and node-specific source trails—not inflation of the node count.

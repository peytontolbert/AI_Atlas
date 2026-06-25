# Alignment, Safety and Evaluation Coverage Review

## Scope Boundary

This review covers the `alignment` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 20 |
| Node packets present | 20 |
| Node review files present | 20 |
| Sentence review ledger rows | 180 |
| Sentence reviews in node review files | 180 |
| Edge review ledger rows targeting this layer | 66 |
| Review verdict mix | supported_by_synthesis: 79, verified: 101 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_c2pa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: C2PA Technical Specification. |
| `ref_ddia` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Designing Data-Intensive Applications. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_dpo` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Direct Preference Optimization. |
| `ref_formalml` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Formal Methods for Machine Learning: A Survey. |
| `ref_llmjudge` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey on LLM-as-a-Judge. |
| `ref_nist` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Risk Management Framework 1.0. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_react` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: ReAct: Synergizing Reasoning and Acting in Language Models. |
| `ref_rlhf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Training language models to follow instructions with human feedback. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |
| `ref_watermark` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Watermark for Large Language Models. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Adversarial robustness & security testing | accepted_node | `adversarial_security_eval` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Benchmarks, test suites & task metrics | accepted_node | `benchmarks_metrics` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Calibration, uncertainty & risk evaluation | accepted_node | `calibration_evaluation` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Ablation, interventions & causal analysis | accepted_node | `causal_ablation` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Content credentials, signing & provenance | accepted_node | `content_provenance` | First-class node in `alignment` with packet and sentence review coverage. | `ref_c2pa` |
| Evaluation-driven development & release gates | accepted_node | `eval_driven_development` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Fairness, bias & subgroup analysis | accepted_node | `fairness_bias` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Formal verification of agents & plans | accepted_node | `formal_agent_verification` | First-class node in `alignment` with packet and sentence review coverage. | `ref_formalml` |
| Formal verification of models | accepted_node | `formal_model_verification` | First-class node in `alignment` with packet and sentence review coverage. | `ref_formalml` |
| Human evaluation & preference studies | accepted_node | `human_evaluation` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Feature attribution & interpretability | accepted_node | `interpretability` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| LLM-as-judge & automated critique | accepted_node | `llm_as_judge` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist`, `ref_llmjudge` |
| Mechanistic interpretability & circuit analysis | accepted_node | `mechanistic_interpretability` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Generation-time watermarking | accepted_node | `output_watermarking` | First-class node in `alignment` with packet and sentence review coverage. | `ref_watermark` |
| Privacy, governance, licensing & audit | accepted_node | `privacy_governance` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Red teaming, abuse testing & threat modeling | accepted_node | `red_teaming` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Reproducibility, drift & continuous monitoring | accepted_node | `repro_monitoring` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Robustness, distribution shift & OOD evaluation | accepted_node | `robustness_ood` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |
| Runtime assurance, monitors & safety envelopes | accepted_node | `runtime_assurance` | First-class node in `alignment` with packet and sentence review coverage. | `ref_formalml`, `ref_nist` |
| Safety policies, constitutional constraints & alignment | accepted_node | `safety_policy_alignment` | First-class node in `alignment` with packet and sentence review coverage. | `ref_nist` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `alignment` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Alignment, Safety and Evaluation | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

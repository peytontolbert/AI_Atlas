# Data and Representations Coverage Review

## Scope Boundary

This review covers the `representation` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 19 |
| Node packets present | 19 |
| Node review files present | 19 |
| Sentence review ledger rows | 167 |
| Sentence reviews in node review files | 167 |
| Edge review ledger rows targeting this layer | 57 |
| Review verdict mix | supported_by_synthesis: 74, verified: 93 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_ddia` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Designing Data-Intensive Applications. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_domainrand` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. |
| `ref_formalml` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Formal Methods for Machine Learning: A Survey. |
| `ref_gnn` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Relational inductive biases, deep learning, and graph networks. |
| `ref_koller` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Graphical Models. |
| `ref_moe` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. |
| `ref_nerf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. |
| `ref_nist` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Risk Management Framework 1.0. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_prml` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Pattern Recognition and Machine Learning. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rt2` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. |
| `ref_sim2real` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Waveforms, audio & spectrograms | accepted_node | `audio_signals` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Datasets, sampling & splits | accepted_node | `datasets_sampling` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Distributions, uncertainty & beliefs | accepted_node | `distributions_uncertainty` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Embeddings & distributed representations | accepted_node | `embeddings` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Graphs, hypergraphs & relational data | accepted_node | `graphs_hypergraphs` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Knowledge graphs, ontologies & schemas | accepted_node | `knowledge_graphs` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Latent variables & hidden state | accepted_node | `latent_variables` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Markov chains, MDPs, POMDPs & belief states | accepted_node | `markov_decision_processes` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Multimodal, simulated & streaming data | accepted_node | `multimodal_simulated_streams` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Positional, temporal & coordinate encodings | accepted_node | `positional_encodings` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Programs, ASTs, bytecode & intermediate representations | accepted_node | `programs_ast_ir` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Schemas, grammars & formal output languages | accepted_node | `schemas_grammars_constraints` | First-class node in `representation` with packet and sentence review coverage. | `ref_aima`, `ref_structured` |
| Sequences, events & time series | accepted_node | `sequences_time` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Sets, point clouds & meshes | accepted_node | `sets_pointclouds` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Sparse coding & compositional representations | accepted_node | `sparse_distributed_codes` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Images, video & spatial grids | accepted_node | `spatial_grids` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Labels, targets, rewards & preferences | accepted_node | `supervision_signals` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Scalars, vectors, matrices & tensors | accepted_node | `tensors` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |
| Tokens, vocabularies & symbolic units | accepted_node | `tokens_vocab` | First-class node in `representation` with packet and sentence review coverage. | `ref_pml` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `representation` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Data and Representations | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

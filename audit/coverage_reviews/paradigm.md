# Learning Paradigms Coverage Review

## Scope Boundary

This review covers the `paradigm` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 23 |
| Node packets present | 23 |
| Node review files present | 23 |
| Sentence review ledger rows | 208 |
| Sentence reviews in node review files | 208 |
| Edge review ledger rows targeting this layer | 84 |
| Review verdict mix | supported_by_synthesis: 59, verified: 149 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_diffusion` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Denoising Diffusion Probabilistic Models. |
| `ref_domainrand` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. |
| `ref_dpo` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Direct Preference Optimization. |
| `ref_flow` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Flow Matching for Generative Modeling. |
| `ref_gan` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Generative Adversarial Nets. |
| `ref_jepa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture. |
| `ref_nas` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Neural Architecture Search: A Survey. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rlhf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Training language models to follow instructions with human feedback. |
| `ref_sim2real` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey. |
| `ref_testtime` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. |
| `ref_vae` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Auto-Encoding Variational Bayes. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Active learning & curriculum learning | accepted_node | `active_curriculum_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| AutoML & automated model design | accepted_node | `automl_paradigm` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_nas` |
| Causal representation learning | accepted_node | `causal_representation_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Continual & online learning | accepted_node | `continual_online_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Contrastive learning | accepted_node | `contrastive_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Evolutionary, swarm & population-based learning | accepted_node | `evolutionary_population_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Federated & privacy-preserving learning | accepted_node | `federated_private_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Generative modeling | accepted_node | `generative_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima`, `ref_vae`, `ref_gan`, `ref_diffusion`, `ref_flow` |
| Imitation & inverse reinforcement learning | accepted_node | `imitation_inverse_rl` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| In-context & test-time learning | accepted_node | `incontext_testtime_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima`, `ref_testtime` |
| Perceptron, Hebbian, Oja & spike-timing plasticity | accepted_node | `local_plasticity_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Meta-learning | accepted_node | `meta_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Model-based reinforcement learning | accepted_node | `model_based_rl` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_rlbook` |
| Neuro-symbolic & physics-informed learning | accepted_node | `neurosymbolic_physics_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Predictive representation learning / JEPA | accepted_node | `predictive_jepa_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima`, `ref_jepa` |
| Preference learning | accepted_node | `preference_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima`, `ref_rlhf`, `ref_dpo` |
| Reinforcement learning | accepted_node | `reinforcement_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_rlbook` |
| Self-supervised learning | accepted_node | `self_supervised_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Semi-supervised & weak supervision | accepted_node | `semi_weak_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Sim-to-real, real-to-sim & digital transfer | accepted_node | `sim_to_real_transfer` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_sim2real`, `ref_domainrand` |
| Supervised learning | accepted_node | `supervised_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Transfer, multitask & domain adaptation | accepted_node | `transfer_multitask_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |
| Unsupervised learning | accepted_node | `unsupervised_learning` | First-class node in `paradigm` with packet and sentence review coverage. | `ref_aima` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `paradigm` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Learning Paradigms | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

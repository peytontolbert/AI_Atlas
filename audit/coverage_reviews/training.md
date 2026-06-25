# Training, Adaptation and Compression Coverage Review

## Scope Boundary

This review covers the `training` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 27 |
| Node packets present | 27 |
| Node review files present | 27 |
| Sentence review ledger rows | 247 |
| Sentence reviews in node review files | 247 |
| Edge review ledger rows targeting this layer | 101 |
| Review verdict mix | supported_by_synthesis: 68, verified: 179 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_chinchilla` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Training Compute-Optimal Large Language Models. |
| `ref_diffusion` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Denoising Diffusion Probabilistic Models. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_domainrand` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. |
| `ref_dpo` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Direct Preference Optimization. |
| `ref_flow` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Flow Matching for Generative Modeling. |
| `ref_gan` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Generative Adversarial Nets. |
| `ref_grpo` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. |
| `ref_lora` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: LoRA: Low-Rank Adaptation of Large Language Models. |
| `ref_modelmerge` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time. |
| `ref_moe` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. |
| `ref_nas` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Neural Architecture Search: A Survey. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rlhf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Training language models to follow instructions with human feedback. |
| `ref_rlvr` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning with Verifiable Rewards: A Survey. |
| `ref_scaling` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling Laws for Neural Language Models. |
| `ref_sim2real` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey. |
| `ref_testtime` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. |
| `ref_vae` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Auto-Encoding Variational Bayes. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Adam, Adafactor & adaptive optimizers | accepted_node | `adaptive_optimizers` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Data augmentation & synthetic-data generation | accepted_node | `augmentation_synthetic` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Automatic differentiation & backpropagation | accepted_node | `autodiff_backprop` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Checkpointing, recovery & experiment state | accepted_node | `checkpoint_recovery` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Compute-optimal scaling & training allocation | accepted_node | `compute_optimal_training` | First-class node in `training` with packet and sentence review coverage. | `ref_chinchilla` |
| Continual learning & test-time adaptation pipelines | accepted_node | `continual_testtime_adaptation` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Curricula, data mixtures & sampling schedules | accepted_node | `curriculum_data_mixtures` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Data collection, curation & filtering | accepted_node | `data_curation` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Deduplication, contamination control & provenance | accepted_node | `dedup_decontamination` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Knowledge distillation, pruning & sparsification | accepted_node | `distillation_pruning` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Distributed, mixed-precision & memory-efficient training | accepted_node | `distributed_mixed_precision` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Domain randomization & simulation curricula | accepted_node | `domain_randomization` | First-class node in `training` with packet and sentence review coverage. | `ref_domainrand` |
| Direct and online preference optimization | accepted_node | `dpo_posttraining` | First-class node in `training` with packet and sentence review coverage. | `ref_dpo` |
| Group Relative Policy Optimization (GRPO) | accepted_node | `grpo` | First-class node in `training` with packet and sentence review coverage. | `ref_grpo` |
| Model merging & weight-space composition | accepted_node | `model_merging` | First-class node in `training` with packet and sentence review coverage. | `ref_modelmerge` |
| Neural architecture search | accepted_node | `neural_architecture_search` | First-class node in `training` with packet and sentence review coverage. | `ref_nas` |
| Parameter-efficient tuning, adapters & LoRA | accepted_node | `peft_lora` | First-class node in `training` with packet and sentence review coverage. | `ref_lora` |
| Large-scale pretraining | accepted_node | `pretraining` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Quantization-aware training & low-precision adaptation | accepted_node | `quantization_training` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Regularization, dropout & weight decay | accepted_node | `regularization` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Reward-model training, RLHF & RLAIF | accepted_node | `reward_rlhf` | First-class node in `training` with packet and sentence review coverage. | `ref_rlhf` |
| Reinforcement learning with verifiable rewards (RLVR) | accepted_node | `rlvr` | First-class node in `training` with packet and sentence review coverage. | `ref_rlvr`, `ref_grpo` |
| Learning-rate schedules, warmup & stabilization | accepted_node | `schedules_stabilization` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Supervised fine-tuning & instruction tuning | accepted_node | `sft_instruction` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| SGD, momentum & stochastic optimization | accepted_node | `sgd_variants` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |
| Task vectors & parameter arithmetic | accepted_node | `task_arithmetic` | First-class node in `training` with packet and sentence review coverage. | `ref_modelmerge` |
| Tokenization, serialization & packing | accepted_node | `tokenization_serialization` | First-class node in `training` with packet and sentence review coverage. | `ref_dlbook` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `training` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Training, Adaptation and Compression | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

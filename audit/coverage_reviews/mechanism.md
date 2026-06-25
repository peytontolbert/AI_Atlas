# Computational Primitives and Mechanisms Coverage Review

## Scope Boundary

This review covers the `mechanism` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 37 |
| Node packets present | 37 |
| Node review files present | 37 |
| Sentence review ledger rows | 321 |
| Sentence reviews in node review files | 321 |
| Edge review ledger rows targeting this layer | 111 |
| Review verdict mix | supported_by_synthesis: 79, verified: 242 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_flow` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Flow Matching for Generative Modeling. |
| `ref_mamba` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mamba: Linear-Time Sequence Modeling with Selective State Spaces. |
| `ref_mod` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Adaptive depth, early exit & token skipping | accepted_node | `adaptive_depth_early_exit` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_mod` |
| Adversarial examples & adversarial training | accepted_node | `adversarial_training_mechanism` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Affine transforms & dense layers | accepted_node | `affine_dense` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Autoregressive decoding | accepted_node | `autoregressive_decoding` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Boolean circuits & differentiable logic gates | accepted_node | `boolean_logic_gates` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Caches, APIs & tool interfaces | accepted_node | `cache_tool_interfaces` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Constraint propagation, logic & program execution | accepted_node | `constraint_program_execution` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Continuous normalizing flows & learned vector fields | accepted_node | `continuous_flows` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Convolution & local filters | accepted_node | `convolution` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Cross-attention & co-attention | accepted_node | `cross_attention` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Reparameterization & differentiable sampling | accepted_node | `differentiable_sampling` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Differentiable ODE/PDE/SDE solvers | accepted_node | `differentiable_solvers` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Denoising diffusion & stochastic corruption | accepted_node | `diffusion_denoising` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Sparse, local, linear & recurrent attention | accepted_node | `efficient_attention` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Equivariance, invariance & geometric priors | accepted_node | `equivariance_invariance` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| External retrieval & ranking | accepted_node | `external_retrieval` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Gating & multiplicative control | accepted_node | `gating` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Grammar- and schema-constrained decoding | accepted_node | `grammar_constrained_decoding` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_structured` |
| Kernels & implicit feature maps | accepted_node | `kernel_methods` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Causal, masked & structured masking | accepted_node | `masking` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Differentiable memory read/write | accepted_node | `memory_read_write` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Message passing & neighborhood aggregation | accepted_node | `message_passing` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Nonlinear activations | accepted_node | `nonlinear_activations` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Normalization & standardization | accepted_node | `normalization` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Pooling & local aggregation | accepted_node | `pooling` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Relative position, RoPE, ALiBi & coordinate mechanisms | accepted_node | `positional_mechanisms` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Recurrence & feedback state | accepted_node | `recurrence` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Recursive partitioning & ensembling | accepted_node | `recursive_partition_ensemble` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Striding, pooling, patchification & up/downsampling | accepted_node | `resampling_patchification` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Residual, skip & highway connections | accepted_node | `residual_connections` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Routing, conditional computation & mixture-of-experts | accepted_node | `routing_moe` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Search, sampling & decoding procedures | accepted_node | `search_sampling_decoding` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Selective state-space scan | accepted_node | `selective_scan` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_mamba` |
| Self-attention | accepted_node | `self_attention` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Fourier, wavelet & spectral transforms | accepted_node | `spectral_transforms` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| Spiking neurons & temporal coding | accepted_node | `spiking_temporal_dynamics` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |
| State-space transitions | accepted_node | `state_space_transition` | First-class node in `mechanism` with packet and sentence review coverage. | `ref_dlbook` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `mechanism` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Computational Primitives and Mechanisms | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

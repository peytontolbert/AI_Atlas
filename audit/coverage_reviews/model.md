# Model and Architecture Families Coverage Review

## Scope Boundary

This review covers the `model` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 52 |
| Node packets present | 52 |
| Node review files present | 52 |
| Sentence review ledger rows | 465 |
| Sentence reviews in node review files | 465 |
| Edge review ledger rows targeting this layer | 192 |
| Review verdict mix | supported_by_synthesis: 149, verified: 316 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_bert` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: BERT: Pre-training of Deep Bidirectional Transformers. |
| `ref_diffusion` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Denoising Diffusion Probabilistic Models. |
| `ref_diffusion_lm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Diffusion-LM Improves Controllable Text Generation. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_dreamer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mastering Diverse Domains through World Models. |
| `ref_flow` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Flow Matching for Generative Modeling. |
| `ref_fno` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Fourier Neural Operator for Parametric Partial Differential Equations. |
| `ref_gan` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Generative Adversarial Nets. |
| `ref_gnn` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Relational inductive biases, deep learning, and graph networks. |
| `ref_jepa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture. |
| `ref_koller` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Graphical Models. |
| `ref_lstm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Long Short-Term Memory. |
| `ref_mamba` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mamba: Linear-Time Sequence Modeling with Selective State Spaces. |
| `ref_mdlm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Simple and Effective Masked Diffusion Language Models. |
| `ref_mod` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models. |
| `ref_moe` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. |
| `ref_nerf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. |
| `ref_neuralode` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Neural Ordinary Differential Equations. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_react` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: ReAct: Synergizing Reasoning and Acting in Language Models. |
| `ref_resnet` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Deep Residual Learning for Image Recognition. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rt2` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. |
| `ref_s4` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Efficiently Modeling Long Sequences with Structured State Spaces. |
| `ref_sim2real` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |
| `ref_unet` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: U-Net: Convolutional Networks for Biomedical Image Segmentation. |
| `ref_vae` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Auto-Encoding Variational Bayes. |
| `ref_xlstm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: xLSTM: Extended Long Short-Term Memory. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Autoencoders | accepted_node | `autoencoder` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Bayesian networks, MRFs & factor graphs | accepted_node | `bayesian_factor_graphs` | First-class node in `model` with packet and sentence review coverage. | `ref_koller` |
| k-means, mixture models & clustering | accepted_node | `clustering_mixture_models` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Convolutional neural networks | accepted_node | `cnn` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Decoder-only causal transformers | accepted_node | `decoder_only_transformer` | First-class node in `model` with packet and sentence review coverage. | `ref_transformer` |
| Diffusion and masked-generative language models | accepted_node | `diffusion_language_model` | First-class node in `model` with packet and sentence review coverage. | `ref_diffusion`, `ref_diffusion_lm`, `ref_mdlm` |
| Diffusion & score-based models | accepted_node | `diffusion_model` | First-class node in `model` with packet and sentence review coverage. | `ref_diffusion` |
| PCA, ICA, NMF & manifold reduction | accepted_node | `dimensionality_reduction` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Encoder–decoder transformers | accepted_node | `encoder_decoder_transformer` | First-class node in `model` with packet and sentence review coverage. | `ref_transformer` |
| Encoder-only bidirectional transformers | accepted_node | `encoder_only_transformer` | First-class node in `model` with packet and sentence review coverage. | `ref_bert` |
| Energy-based, Hopfield & Boltzmann models | accepted_node | `energy_hopfield` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Expert systems, production rules & rule engines | accepted_node | `expert_rule_systems` | First-class node in `model` with packet and sentence review coverage. | `ref_aima` |
| Normalizing, rectified & flow-matching models | accepted_node | `flow_based_model` | First-class node in `model` with packet and sentence review coverage. | `ref_flow` |
| Generative adversarial networks | accepted_node | `gan` | First-class node in `model` with packet and sentence review coverage. | `ref_gan` |
| Gaussian processes | accepted_node | `gaussian_processes` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Graph neural networks | accepted_node | `gnn` | First-class node in `model` with packet and sentence review coverage. | `ref_gnn` |
| Graph transformers | accepted_node | `graph_transformer` | First-class node in `model` with packet and sentence review coverage. | `ref_gnn`, `ref_transformer` |
| Hidden Markov models & CRFs | accepted_node | `hmm_crf` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Transformer–SSM & recurrent hybrid models | accepted_node | `hybrid_transformer_ssm` | First-class node in `model` with packet and sentence review coverage. | `ref_mamba`, `ref_xlstm` |
| Joint-embedding predictive architectures | accepted_node | `jepa_model` | First-class node in `model` with packet and sentence review coverage. | `ref_jepa` |
| k-NN & Naive Bayes | accepted_node | `knn_naive_bayes` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Linear models & generalized linear models | accepted_node | `linear_glm` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| LSTMs & GRUs | accepted_node | `lstm_gru` | First-class node in `model` with packet and sentence review coverage. | `ref_lstm` |
| Selective state-space models (Mamba family) | accepted_node | `mamba_selective_ssm` | First-class node in `model` with packet and sentence review coverage. | `ref_mamba` |
| Matrix factorization & topic models | accepted_node | `matrix_factor_topic` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Memory-augmented neural networks | accepted_node | `memory_augmented_nn` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Mixture-of-Depths | accepted_node | `mixture_of_depths` | First-class node in `model` with packet and sentence review coverage. | `ref_mod` |
| Multilayer perceptrons | accepted_node | `mlp` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Mixture-of-experts models | accepted_node | `moe_model` | First-class node in `model` with packet and sentence review coverage. | `ref_moe` |
| Multimodal foundation models | accepted_node | `multimodal_foundation` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Neural fields & radiance-field models | accepted_node | `neural_fields_nerf` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook`, `ref_nerf` |
| Neural ODEs, CDEs & SDEs | accepted_node | `neural_ode_cde` | First-class node in `model` with packet and sentence review coverage. | `ref_neuralode` |
| Neural operators, FNOs & PINNs | accepted_node | `neural_operator_pinn` | First-class node in `model` with packet and sentence review coverage. | `ref_fno` |
| Neuro-symbolic models | accepted_node | `neurosymbolic_system_model` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Perceptrons & single-layer neural classifiers | accepted_node | `perceptron_model` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Probabilistic & differentiable programming | accepted_node | `probabilistic_programming` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Reservoir computing (ESN / LSM) | accepted_node | `reservoir_computing` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| ResNets & DenseNets | accepted_node | `resnet_densenet` | First-class node in `model` with packet and sentence review coverage. | `ref_resnet` |
| Recurrent neural networks | accepted_node | `rnn` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Self-organizing maps & competitive learning | accepted_node | `self_organizing_maps` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Spiking neural networks | accepted_node | `snn` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Structured state-space models (S4 family) | accepted_node | `structured_ssm` | First-class node in `model` with packet and sentence review coverage. | `ref_s4` |
| Support vector & kernel machines | accepted_node | `svm_kernel_models` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Transformers | accepted_node | `transformer` | First-class node in `model` with packet and sentence review coverage. | `ref_transformer` |
| Decision trees, random forests & boosted trees | accepted_node | `tree_ensemble_models` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| U-Nets & encoder–decoder convnets | accepted_node | `unet` | First-class node in `model` with packet and sentence review coverage. | `ref_unet` |
| Variational autoencoders | accepted_node | `vae` | First-class node in `model` with packet and sentence review coverage. | `ref_vae` |
| Vision–language–action models | accepted_node | `vision_language_action_model` | First-class node in `model` with packet and sentence review coverage. | `ref_react`, `ref_sim2real`, `ref_rt2` |
| Vision Transformers & Perceiver-style latent models | accepted_node | `vision_transformer_perceiver` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| VQ-VAE & learned discrete tokenizers | accepted_node | `vqvae_tokenizer` | First-class node in `model` with packet and sentence review coverage. | `ref_dlbook` |
| Latent world models & predictive dynamics | accepted_node | `world_model` | First-class node in `model` with packet and sentence review coverage. | `ref_dreamer` |
| xLSTM & linear-recurrent hybrids | accepted_node | `xlstm_rwkv` | First-class node in `model` with packet and sentence review coverage. | `ref_xlstm` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `model` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Model and Architecture Families | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

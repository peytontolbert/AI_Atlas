# Infrastructure and Serving Coverage Review

## Scope Boundary

This review covers the `infrastructure` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 22 |
| Node packets present | 22 |
| Node review files present | 22 |
| Sentence review ledger rows | 207 |
| Sentence reviews in node review files | 207 |
| Edge review ledger rows targeting this layer | 87 |
| Review verdict mix | supported_by_synthesis: 63, verified: 144 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_ann` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. |
| `ref_c2pa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: C2PA Technical Specification. |
| `ref_cuda_guide` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: NVIDIA CUDA C Programming Guide. |
| `ref_ddia` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Designing Data-Intensive Applications. |
| `ref_digital_twin_ai` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Simulation by Digital Twins: Systematic Survey, Reference Framework, and Mapping to a Standardized Architecture. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_gptq` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. |
| `ref_lora` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: LoRA: Low-Rank Adaptation of Large Language Models. |
| `ref_megatron` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. |
| `ref_modelmerge` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time. |
| `ref_nist` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Risk Management Framework 1.0. |
| `ref_pagedattention` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Efficient Memory Management for Large Language Model Serving with PagedAttention. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_rocm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: ROCm Documentation. |
| `ref_scenario_generation` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Foundation Models in Autonomous Driving: A Survey on Scenario Generation and Scenario Analysis. |
| `ref_smoothquant` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. |
| `ref_speculative_sampling` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Accelerating Large Language Model Decoding with Speculative Sampling. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |
| `ref_tpu` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: In-Datacenter Performance Analysis of a Tensor Processing Unit. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| GPUs, TPUs & AI accelerators | accepted_node | `accelerators` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_tpu`, `ref_cuda_guide` |
| API gateways, tool registries & secure connectors | accepted_node | `api_tool_gateway` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Batching, admission control & GPU scheduling | accepted_node | `batching_scheduling` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Checkpoint, adapter & expert composition | accepted_node | `checkpoint_composition` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_lora`, `ref_modelmerge` |
| Graph compilers, runtimes & operator fusion | accepted_node | `compilers_runtimes` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Cryptographic signing & tamper-evident logs | accepted_node | `cryptographic_signing` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_c2pa`, `ref_ddia` |
| Distributed data pipelines & streaming | accepted_node | `data_pipelines` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Edge, on-device & neuromorphic deployment | accepted_node | `edge_ondevice` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Fault tolerance, security, energy & cost optimization | accepted_node | `fault_energy_ops` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| CUDA, ROCm, Triton & custom kernels | accepted_node | `gpu_kernels` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_cuda_guide`, `ref_rocm` |
| Model servers & inference runtimes | accepted_node | `model_serving` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Observability, tracing & evaluation harnesses | accepted_node | `observability_eval_harness` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Workflow, cluster & job orchestration | accepted_node | `orchestration` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Paged attention & KV-memory management | accepted_node | `paged_attention` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_pagedattention` |
| Tensor, pipeline, sequence & expert parallel inference | accepted_node | `parallel_inference` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_megatron` |
| Quantized inference & compressed deployment | accepted_node | `quantized_inference` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_gptq`, `ref_smoothquant` |
| Model registry, versioning & MLOps / LLMOps | accepted_node | `registry_mlops` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Simulation farms, digital environments & scenario generation | accepted_node | `simulation_infrastructure` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_digital_twin_ai`, `ref_scenario_generation` |
| Speculative, parallel & assisted decoding | accepted_node | `speculative_decoding` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_speculative_sampling` |
| Object storage, sharding & checkpoints | accepted_node | `storage_checkpoints` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |
| Structured-decoding runtimes | accepted_node | `structured_decoding_runtime` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_structured` |
| Vector-search and retrieval services | accepted_node | `vector_retrieval_service` | First-class node in `infrastructure` with packet and sentence review coverage. | `ref_ddia` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `infrastructure` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Infrastructure and Serving | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

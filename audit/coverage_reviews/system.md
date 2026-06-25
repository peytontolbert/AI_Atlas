# Systems and Applications Coverage Review

## Scope Boundary

This review covers the `system` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 32 |
| Node packets present | 32 |
| Node review files present | 32 |
| Sentence review ledger rows | 477 |
| Sentence reviews in node review files | 477 |
| Edge review ledger rows targeting this layer | 273 |
| Review verdict mix | supported_by_synthesis: 355, verified: 122 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_bert` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: BERT: Pre-training of Deep Bidirectional Transformers. |
| `ref_c2pa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: C2PA Technical Specification. |
| `ref_chinchilla` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Training Compute-Optimal Large Language Models. |
| `ref_ddia` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Designing Data-Intensive Applications. |
| `ref_diffusion` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Denoising Diffusion Probabilistic Models. |
| `ref_digital_twin_ai` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Simulation by Digital Twins: Systematic Survey, Reference Framework, and Mapping to a Standardized Architecture. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_domainrand` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. |
| `ref_dreamer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mastering Diverse Domains through World Models. |
| `ref_flow` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Flow Matching for Generative Modeling. |
| `ref_fno` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Fourier Neural Operator for Parametric Partial Differential Equations. |
| `ref_formalml` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Formal Methods for Machine Learning: A Survey. |
| `ref_gnn` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Relational inductive biases, deep learning, and graph networks. |
| `ref_grpo` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. |
| `ref_jepa` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture. |
| `ref_koller` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Graphical Models. |
| `ref_lstm` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Long Short-Term Memory. |
| `ref_mamba` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mamba: Linear-Time Sequence Modeling with Selective State Spaces. |
| `ref_nerf` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. |
| `ref_neuralode` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Neural Ordinary Differential Equations. |
| `ref_nist` | Standard / official report | 2026-06-25 | Used by layer node packets/reviews: AI Risk Management Framework 1.0. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_prml` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Pattern Recognition and Machine Learning. |
| `ref_rag` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. |
| `ref_react` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: ReAct: Synergizing Reasoning and Acting in Language Models. |
| `ref_resnet` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Deep Residual Learning for Image Recognition. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rlvr` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning with Verifiable Rewards: A Survey. |
| `ref_rt2` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. |
| `ref_s4` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Efficiently Modeling Long Sequences with Structured State Spaces. |
| `ref_scaling` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling Laws for Neural Language Models. |
| `ref_scenario_generation` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Foundation Models in Autonomous Driving: A Survey on Scenario Generation and Scenario Analysis. |
| `ref_sim2real` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |
| `ref_testtime` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. |
| `ref_tot` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Tree of Thoughts: Deliberate Problem Solving with Large Language Models. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |
| `ref_vae` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Auto-Encoding Variational Bayes. |
| `ref_watermark` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Watermark for Large Language Models. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Autonomous research & AI scientist systems | accepted_node | `autonomous_research` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Autonomous vehicles, drones & navigation | accepted_node | `autonomous_vehicles` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Conversational assistants & chatbots | accepted_node | `chat_assistants` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Code models, copilots & repository intelligence | accepted_node | `code_assistants` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Browser, desktop & computer-use agents | accepted_node | `computer_use_agents` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Cybersecurity, finance & operational risk AI | accepted_node | `cyber_finance` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Document intelligence & information extraction | accepted_node | `document_intelligence` | First-class node in `system` with packet and sentence review coverage. | `ref_bert`, `ref_transformer` |
| Drug discovery, protein & molecular design | accepted_node | `drug_protein` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Neuromorphic, sensor & edge intelligence | accepted_node | `edge_neuromorphic` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Tutoring, translation & knowledge work | accepted_node | `education_translation` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Game-playing, control & simulation agents | accepted_node | `game_control` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Image generation, editing & design | accepted_node | `image_generation` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Knowledge graphs, semantic search & relational reasoning | accepted_node | `knowledge_graph_systems` | First-class node in `system` with packet and sentence review coverage. | `ref_koller`, `ref_rag` |
| Large language models | accepted_node | `llms` | First-class node in `system` with packet and sentence review coverage. | `ref_transformer`, `ref_scaling`, `ref_chinchilla` |
| Medical imaging & clinical decision support | accepted_node | `medical_ai` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Multi-agent systems & organizational intelligence | accepted_node | `multiagent_systems` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Multimodal assistants & vision-language systems | accepted_node | `multimodal_assistants` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Recommendation, ranking & personalization | accepted_node | `recommender_systems` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Robotics & embodied AI | accepted_node | `robotics` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Scientific ML, simulators & digital twins | accepted_node | `scientific_digital_twins` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Neural search, RAG & question answering | accepted_node | `search_rag_qa` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Simulation, operations research & wargaming | accepted_node | `simulation_wargaming` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Autonomous software-engineering agents | accepted_node | `software_agents` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Speech synthesis, voice & music generation | accepted_node | `speech_audio_generation` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Speech recognition & spoken-language understanding | accepted_node | `speech_recognition` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Tabular predictive analytics & decision support | accepted_node | `tabular_predictive_analytics` | First-class node in `system` with packet and sentence review coverage. | `ref_prml`, `ref_pml` |
| Automated theorem proving & mathematical AI | accepted_node | `theorem_math_systems` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Time-series forecasting, anomaly & fraud detection | accepted_node | `timeseries_anomaly` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Verified and assurance-gated agents | accepted_node | `verified_agentic_systems` | First-class node in `system` with packet and sentence review coverage. | `ref_formalml`, `ref_nist` |
| Video generation & simulation synthesis | accepted_node | `video_generation` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |
| Computer vision, perception & scene understanding | accepted_node | `vision_perception` | First-class node in `system` with packet and sentence review coverage. | `ref_dlbook`, `ref_transformer` |
| Weather, climate & geospatial forecasting | accepted_node | `weather_climate` | First-class node in `system` with packet and sentence review coverage. | `ref_aima` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `system` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Systems and Applications | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

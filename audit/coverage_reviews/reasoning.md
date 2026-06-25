# Reasoning, Planning and Agency Coverage Review

## Scope Boundary

This review covers the `reasoning` layer of the AI Dependency Atlas as of 2026-06-25. The completeness claim is bounded to the repository corpus, the canonical atlas graph in `data/atlas.json`, the per-node packets in `audit/node_packets/`, the sentence reviews in `audit/node_reviews/`, and the edge-review ledger. It is not a claim that all possible AI concepts or future literature are universally exhausted.

## Coverage Summary

| Metric | Current value |
|---|---:|
| Atlas nodes in layer | 26 |
| Node packets present | 26 |
| Node review files present | 26 |
| Sentence review ledger rows | 232 |
| Sentence reviews in node review files | 232 |
| Edge review ledger rows targeting this layer | 86 |
| Review verdict mix | supported_by_synthesis: 68, verified: 164 |
| Nodes missing review entries | None. |

## Sources Searched

| Source | Type | Date checked | Notes |
|---|---|---|---|
| `ref_aima` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Artificial Intelligence: A Modern Approach, 4th ed.. |
| `ref_dlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Deep Learning. |
| `ref_dreamer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Mastering Diverse Domains through World Models. |
| `ref_got` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Graph of Thoughts: Solving Elaborate Problems with Large Language Models. |
| `ref_pml` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Probabilistic Machine Learning: An Introduction. |
| `ref_react` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: ReAct: Synergizing Reasoning and Acting in Language Models. |
| `ref_rlbook` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning: An Introduction, 2nd ed.. |
| `ref_rlvr` | Textbook/survey | 2026-06-25 | Used by layer node packets/reviews: Reinforcement Learning with Verifiable Rewards: A Survey. |
| `ref_structured` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: A Survey of Structured Output Generation from LLMs. |
| `ref_testtime` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. |
| `ref_tot` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Tree of Thoughts: Deliberate Problem Solving with Large Language Models. |
| `ref_transformer` | Primary paper / technical report | 2026-06-25 | Used by layer node packets/reviews: Attention Is All You Need. |

## Candidate Concepts

| Candidate | Disposition | Existing or new node | Rationale | Sources |
|---|---|---|---|---|
| Observe–plan–act agent loops | accepted_node | `agent_loop` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_react` |
| Beam search & constrained decoding | accepted_node | `beam_search` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Best-of-N & verifier-guided selection | accepted_node | `best_of_n_verifier` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_testtime`, `ref_rlvr` |
| Code execution, interpreters & sandboxes | accepted_node | `code_execution` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Constraint satisfaction, SAT & SMT solving | accepted_node | `constraint_sat_smt` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Chain-of-thought & latent reasoning | accepted_node | `cot_latent_reasoning` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Graph search, BFS/DFS & A* | accepted_node | `graph_astar_search` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Graph-of-Thought & non-linear deliberation | accepted_node | `graph_of_thoughts` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_tot`, `ref_got` |
| Human-in-the-loop, permissions & sandboxing | accepted_node | `human_loop_sandbox` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Monte Carlo tree search | accepted_node | `mcts` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Model-predictive control | accepted_node | `model_predictive_control` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Multi-agent coordination, debate & markets | accepted_node | `multiagent_coordination` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| PDDL, STRIPS & hierarchical task-network planning | accepted_node | `pddl_htn_planning` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Program synthesis & code search | accepted_node | `program_synthesis` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| ReAct-style reasoning and acting | accepted_node | `react_reason_act` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Reflection, critique, verifier & repair loops | accepted_node | `reflection_verifier` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Self-consistency & best-of-N inference | accepted_node | `self_consistency` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Skill libraries, workflows & procedural plans | accepted_node | `skill_library` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Structured-output parsing, validation & repair | accepted_node | `structured_output_validation` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_structured` |
| Structured outputs & typed action generation | accepted_node | `structured_outputs` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_structured` |
| Task decomposition & hierarchical reasoning | accepted_node | `task_decomposition` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Test-time compute scaling | accepted_node | `test_time_compute` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_testtime` |
| Theorem proving & symbolic deduction | accepted_node | `theorem_symbolic` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |
| Tool use & function calling | accepted_node | `tool_use_function_calling` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_react` |
| Tree-of-Thought & branch-and-evaluate reasoning | accepted_node | `tree_of_thoughts` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_tot` |
| World-model rollout & imagination | accepted_node | `world_model_rollout` | First-class node in `reasoning` with packet and sentence review coverage. | `ref_aima` |

## Rejected Candidates

| Candidate | Reason | Notes |
|---|---|---|
| None recorded | No unresolved rejected candidate was identified in this bounded review pass. | Future source sweeps should add explicit rejected candidates here when a concept is intentionally excluded, merged, or treated as a subvariant. |

## Missing-Concept Challenges

| Challenge | Resolution | Reviewer | Date |
|---|---|---|---|
| Layer packet/review parity | Resolved: every canonical `reasoning` node has a matching packet and node review file. | codex | 2026-06-25 |
| Source-ledger parity | Resolved: sentence and edge audit ledgers cover this layer; see counts above. | codex | 2026-06-25 |
| Universal exhaustiveness | Not asserted: the atlas is maintained as a bounded, source-audited dependency map rather than a mathematically complete ontology of all AI. | codex | 2026-06-25 |

## Disputes

No disputes recorded for this layer in `audit/disputed_claims.md` as of 2026-06-25.

## Sign-Off

| Reviewer | Area | Date | Status |
|---|---|---|---|
| codex | Reasoning, Planning and Agency | 2026-06-25 | Complete for bounded atlas coverage; continue updating when new sources or candidate concepts are added. |

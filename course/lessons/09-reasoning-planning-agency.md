# Lesson 09: Reasoning, Planning, and Agency

## Learning Outcomes

After this lesson, learners can:

- Design an observe-plan-act loop with state, tools, permissions, and stopping rules.
- Compare model reasoning, search, planning, verification, and code execution.
- Identify where structured outputs and human-in-the-loop controls reduce risk.
- Specify logs and tests required for agent debugging.

## Atlas Nodes

`cot_latent_reasoning`, `self_consistency`, `graph_astar_search`, `beam_search`, `mcts`, `constraint_sat_smt`, `theorem_symbolic`, `program_synthesis`, `code_execution`, `task_decomposition`, `pddl_htn_planning`, `model_predictive_control`, `world_model_rollout`, `tool_use_function_calling`, `react_reason_act`, `agent_loop`, `reflection_verifier`, `multiagent_coordination`, `skill_library`, `human_loop_sandbox`, `test_time_compute`, `best_of_n_verifier`, `tree_of_thoughts`, `graph_of_thoughts`, `structured_output_validation`, `structured_outputs`

## Prerequisites

Learners should understand objectives, decoding, tools, and evaluation.

## Core Concepts

- Agent systems repeatedly observe, decide, act, and update state.
- Structured outputs and typed tools make actions inspectable.
- Search and planning explore alternatives rather than accepting one sample.
- Reflection and verifier loops catch some failures but add cost and complexity.
- Code execution and external tools require permissions, sandboxing, and recovery.
- Multi-agent workflows introduce coordination and accountability questions.

## Teaching Plan

1. Start with a one-shot assistant and show why it fails on multi-step tasks.
2. Add state, tools, and an observe-plan-act loop.
3. Add search, verification, and repair.
4. Add sandbox and human approval boundaries.
5. Discuss logging, replay, and incident analysis.

## Guided Discussion

- What state must the system remember?
- What can the model decide alone, and what requires a tool or human?
- Where can actions be validated before execution?
- What is the stopping condition?
- What logs are needed to debug a bad action?

## Lab

Design a minimal agent loop for a coding or research task.

Include:

- State fields.
- Available tools.
- Permission boundaries.
- Planner or search strategy.
- Verification step.
- Stopping conditions.
- Log format.

## Assessment Questions

1. What distinguishes an agent loop from a single tool call?
2. Why do structured outputs reduce ambiguity but not guarantee correctness?
3. What is one safe failure mode for code execution?
4. Why can verifier loops amplify cost?
5. What should be logged for replay and audit?

## Deliverable

An agent loop design sketch.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Describes an agent as a model with tools. |
| Proficient | Defines state, tools, permissions, verification, and stopping rules. |
| Advanced | Designs replayable, auditable, failure-aware agent workflows. |

## Common Failure Mode

Calling a system an agent because it uses a tool once.

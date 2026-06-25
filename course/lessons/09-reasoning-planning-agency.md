# Lesson 09: Reasoning, Planning, and Agency

## Goal

Review how systems move from prediction to multi-step action.

## Review Nodes

`agent_loop`, `tool_use_function_calling`, `structured_outputs`, `react_reason_act`, `cot_latent_reasoning`, `reflection_verifier`, `graph_astar_search`, `beam_search`, `code_execution`, `program_synthesis`, `human_loop_sandbox`, `software_agents`, `code_assistants`

## Key Ideas

- Agent systems repeatedly observe, decide, act, and update state.
- Structured outputs and typed tools make actions inspectable and enforceable.
- Search and planning explore alternatives rather than accepting one sample.
- Reflection and verifier loops catch some failures but add cost and complexity.
- Code execution and sandboxing require explicit permission and recovery design.

## Review Checklist

- Can you draw an observe-plan-act loop?
- Can you distinguish model reasoning from external search?
- Can you explain why typed tool schemas reduce ambiguity?
- Can you define a safe failure mode for code execution?
- Can you name what must be logged for agent debugging?

## Exercise

Design a minimal agent loop for a coding task. Include:

- State fields.
- Available tools.
- Permission boundaries.
- Stopping conditions.
- Test or verification step.
- Log format.

## Deliverable

An agent loop design sketch.

## Common Failure Mode

Calling a system an agent because it uses a tool once. Agency requires stateful multi-step control.

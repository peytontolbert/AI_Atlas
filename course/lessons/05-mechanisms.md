# Lesson 05: Computational Primitives and Mechanisms

## Learning Outcomes

After this lesson, learners can:

- Trace data flow through common neural and agent mechanisms.
- Explain attention, recurrence, convolution, gating, decoding, retrieval, and constraints as reusable operations.
- Identify where caching, tool interfaces, and constrained execution change system behavior.
- Draw a mechanism-level diagram for a model or agent.

## Atlas Nodes

`affine_dense`, `nonlinear_activations`, `autodiff_backprop`, `convolution`, `pooling`, `normalization`, `residual_connections`, `gating`, `recurrence`, `state_space_transition`, `self_attention`, `cross_attention`, `efficient_attention`, `positional_mechanisms`, `message_passing`, `routing_moe`, `external_retrieval`, `autoregressive_decoding`, `masking`, `diffusion_denoising`, `constraint_program_execution`, `search_sampling_decoding`, `cache_tool_interfaces`, `grammar_constrained_decoding`

## Prerequisites

Learners should understand tensors, objectives, and model families at a high level.

## Core Concepts

- Dense layers transform features; activations make compositions nonlinear.
- Residual paths, normalization, and schedules stabilize deep computation.
- Attention routes information by content; recurrence and state-space mechanisms carry state over time.
- Decoding transforms scores into outputs.
- Constraints, schemas, caches, and tools move behavior from pure prediction toward controlled action.

## Teaching Plan

1. Draw a transformer block and trace one token through it.
2. Compare attention with recurrence and convolution.
3. Show how decoding changes output even with fixed model weights.
4. Add retrieval, caching, and tool calls as external mechanisms.
5. Discuss where verification or constraints can intercept errors.

## Guided Discussion

- Where does information enter, transform, branch, and exit?
- Which mechanisms change parameters and which only change runtime behavior?
- Why does caching affect cost but not model knowledge?
- How do constraints reduce invalid outputs without guaranteeing correct outputs?
- What failure modes appear when a mechanism is composed into a larger system?

## Lab

Draw or write pseudocode for a transformer-style block plus decoding step.

Required labels:

- Input and output shapes.
- Attention operation.
- Feed-forward operation.
- Residual and normalization paths.
- Cache use during decoding.
- Optional constraint or tool boundary.

## Assessment Questions

1. What are queries, keys, and values used for?
2. How does recurrence differ from attention?
3. Why can decoding strategy change quality and risk?
4. What does a residual connection help preserve?
5. Why is a tool interface a mechanism rather than a model family?

## Deliverable

A mechanism walkthrough diagram or pseudocode file.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Names components without tracing information flow. |
| Proficient | Traces a block and explains each mechanism's role. |
| Advanced | Explains runtime mechanisms, constraints, and failure boundaries. |

## Common Failure Mode

Knowing component names without being able to trace what information flows where.

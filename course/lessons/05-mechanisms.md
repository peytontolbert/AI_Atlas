# Lesson 05: Computational Primitives and Mechanisms

## Goal

Understand the reusable mechanisms that compose modern models and agent systems.

## Review Nodes

`affine_dense`, `nonlinear_activations`, `autodiff_backprop`, `convolution`, `pooling`, `self_attention`, `positional_mechanisms`, `gating`, `recurrence`, `state_space_transition`, `autoregressive_decoding`, `cache_tool_interfaces`, `constraint_program_execution`

## Key Ideas

- Dense layers transform features; activations add nonlinearity.
- Backpropagation moves credit through computation graphs.
- Attention routes information based on content similarity.
- Recurrence and state-space mechanisms carry state across sequence positions.
- Decoding turns model scores into generated outputs.
- Tool interfaces extend computation beyond model weights.

## Review Checklist

- Can you trace the data flow through one neural block?
- Can you explain attention queries, keys, and values?
- Can you compare recurrence with attention for long sequences?
- Can you explain why decoding strategy affects output quality?
- Can you identify where caching changes cost without changing model weights?

## Exercise

Draw or write pseudocode for a transformer block. Label:

- Input and output shapes.
- Attention operation.
- Feed-forward operation.
- Residual paths.
- Normalization.
- Cache use during decoding.

## Deliverable

A block diagram or pseudocode walkthrough.

## Common Failure Mode

Knowing component names without being able to trace information flow.

# Lesson 02: Data and Representations

## Goal

Understand how raw information becomes model-readable structure.

## Review Nodes

`tensors`, `embeddings`, `tokens_vocab`, `tokenization_serialization`, `datasets_sampling`, `supervision_signals`, `sequences_time`, `spatial_grids`, `graphs_hypergraphs`, `programs_ast_ir`, `multimodal_simulated_streams`, `latent_variables`

## Key Ideas

- Representation choices determine what a model can easily learn.
- Tokens, embeddings, tensors, graphs, images, programs, and time series carry different assumptions.
- Dataset construction is part of the model behavior, not an administrative detail.
- Targets, labels, rewards, and preferences encode the behavior being optimized.

## Review Checklist

- Can you explain what is lost during tokenization?
- Can you distinguish sparse, dense, structured, and sequential representations?
- Can you identify leakage risks in dataset splits?
- Can you explain why embeddings support retrieval and similarity search?
- Can you describe how graph structure differs from chunked text?

## Exercise

Take one AI task and describe three representations for it. For each representation, write:

- What information is preserved.
- What information is lost.
- Which model family is naturally suited to it.
- Which evaluation issue it creates.

## Deliverable

A representation comparison table for one task.

## Common Failure Mode

Treating data format as neutral. The format already shapes the solution space.

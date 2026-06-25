# Lesson 02: Data and Representations

## Learning Outcomes

After this lesson, learners can:

- Explain how representation choices shape what a model can learn.
- Compare tensors, tokens, embeddings, graphs, programs, sequences, images, and latent variables.
- Identify information loss, leakage, and bias introduced during dataset construction.
- Choose representations that match a task, model family, and evaluation plan.

## Atlas Nodes

`tensors`, `datasets_sampling`, `supervision_signals`, `sequences_time`, `spatial_grids`, `audio_signals`, `graphs_hypergraphs`, `tokens_vocab`, `embeddings`, `positional_encodings`, `latent_variables`, `distributions_uncertainty`, `knowledge_graphs`, `programs_ast_ir`, `markov_decision_processes`, `multimodal_simulated_streams`, `schemas_grammars_constraints`

## Prerequisites

Learners should understand Lesson 01 vocabulary: tensors, probability, statistics, and objective functions.

## Core Concepts

- Data is not neutral; preprocessing encodes assumptions.
- Tokens make symbolic streams model-readable but can fragment meaning.
- Embeddings make similarity searchable but can hide provenance and uncertainty.
- Graphs preserve entities and relationships that flat chunks may lose.
- Schemas and grammars make structure enforceable for actions and outputs.
- Labels, targets, rewards, and preferences are different supervision signals.

## Teaching Plan

1. Present one raw artifact, such as a support ticket, image, code file, or transaction log.
2. Convert it into three representations.
3. Compare what each representation preserves and destroys.
4. Map each representation to likely model families and objectives.
5. Discuss evaluation errors caused by the representation.

## Guided Discussion

- When is tokenization a lossy compression step?
- Why do embeddings help retrieval but not guarantee truth?
- What changes when examples are connected by graph relations?
- How can train/test splits leak future information?
- What does a schema prevent, and what does it fail to prevent?

## Lab

Choose one task and describe three representations for it.

For each representation, document:

- Preserved information.
- Lost or distorted information.
- Natural model families.
- Evaluation risks.
- Data quality checks.

## Assessment Questions

1. What is the difference between a label, reward, and preference?
2. Why might dense retrieval fail on exact identifiers?
3. How do positional encodings change sequence modeling?
4. When is a knowledge graph more appropriate than chunked text?
5. What is one dataset split mistake that can invalidate an experiment?

## Deliverable

A representation comparison table for one task.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Lists formats without explaining tradeoffs. |
| Proficient | Compares preserved and lost information for multiple representations. |
| Advanced | Connects representation to model family, objective, evaluation, and deployment risk. |

## Common Failure Mode

Treating data format as an implementation detail instead of a modeling decision.

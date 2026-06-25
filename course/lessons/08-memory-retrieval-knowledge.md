# Lesson 08: Memory, Retrieval, and Knowledge

## Learning Outcomes

After this lesson, learners can:

- Separate retrieval quality from generation quality.
- Compare sparse retrieval, dense retrieval, hybrid reranking, vector databases, and graph retrieval.
- Design RAG evaluations with evidence, answer, and citation checks.
- Explain provenance, memory lifecycle, and knowledge editing risks.

## Atlas Nodes

`parametric_memory`, `context_working_memory`, `kv_cache`, `episodic_memory`, `semantic_memory`, `procedural_memory`, `sparse_retrieval`, `dense_retrieval`, `hybrid_reranking`, `vector_database`, `rag`, `graph_rag`, `long_context_compression`, `knowledge_editing`, `provenance_citations`, `external_data_tools`, `memory_lifecycle`

## Prerequisites

Learners should understand representations, embeddings, datasets, and model serving basics.

## Core Concepts

- Retrieval quality and generation quality should be measured separately.
- Sparse retrieval, dense retrieval, and reranking solve different retrieval problems.
- RAG depends on chunking, indexing, query formulation, retrieval, synthesis, and citation.
- Memory can be parametric, contextual, episodic, semantic, or procedural.
- Provenance is part of trust, not a decoration.
- Memory lifecycle controls retention, forgetting, updates, and consolidation.

## Teaching Plan

1. Show a question-answering example with retrieved evidence.
2. Score retrieval before scoring the generated answer.
3. Compare sparse, dense, hybrid, and graph retrieval.
4. Discuss provenance and citation failure modes.
5. Extend the example into long-context and memory lifecycle concerns.

## Guided Discussion

- Did the system retrieve the right evidence?
- Did the answer use the evidence faithfully?
- What does the citation prove?
- What should be forgotten, refreshed, or consolidated?
- When should retrieval use graph structure rather than chunks?

## Lab

Design a RAG evaluation set with at least five queries.

For each query, specify:

- Expected source or evidence.
- Expected answer.
- Retrieval success criterion.
- Generation success criterion.
- Citation requirement.
- Failure label if the answer is wrong.

## Assessment Questions

1. Why can a final answer be correct even when retrieval failed?
2. Why can a citation be present but unfaithful?
3. When does reranking help?
4. What is the difference between context memory and episodic memory?
5. What does graph RAG add to ordinary RAG?

## Deliverable

A retrieval evaluation table.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Evaluates only final answers. |
| Proficient | Separates retrieval, synthesis, and citation metrics. |
| Advanced | Designs memory lifecycle and provenance controls. |

## Common Failure Mode

Treating RAG as solved once chunks are put in a vector database.

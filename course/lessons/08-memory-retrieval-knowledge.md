# Lesson 08: Memory, Retrieval, and Knowledge

## Goal

Understand how systems store, retrieve, cite, and reason over external information.

## Review Nodes

`external_retrieval`, `sparse_retrieval`, `dense_retrieval`, `hybrid_reranking`, `vector_database`, `rag`, `provenance_citations`, `context_working_memory`, `episodic_memory`, `semantic_memory`, `knowledge_graphs`, `graph_rag`, `external_data_tools`

## Key Ideas

- Retrieval quality and generation quality should be measured separately.
- Sparse retrieval, dense retrieval, and reranking solve different parts of search.
- RAG depends on chunking, indexing, query rewriting, retrieval, synthesis, and citation.
- Provenance is part of trust, not a decoration.
- Graph RAG adds relations and paths when chunks are insufficient.

## Review Checklist

- Can you define recall, precision, and answer faithfulness for RAG?
- Can you explain BM25 versus dense vector retrieval?
- Can you identify when reranking is useful?
- Can you explain why citations can be wrong even when retrieval worked?
- Can you describe a task that needs graph retrieval?

## Exercise

Design a RAG evaluation set with at least five queries. For each query, specify:

- Expected source document or evidence.
- Expected answer.
- Retrieval success criterion.
- Generation success criterion.
- Citation requirement.

## Deliverable

A retrieval evaluation table.

## Common Failure Mode

Evaluating only final answers and never checking whether the right evidence was retrieved.

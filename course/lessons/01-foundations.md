# Lesson 01: Mathematical and Computational Foundations

## Learning Outcomes

After this lesson, learners can:

- Explain why linear algebra, calculus, probability, statistics, and optimization appear before models.
- Trace one training update from prediction to loss to gradient to parameter update.
- Identify numerical, statistical, and computational failure modes before debugging model code.
- Connect algorithms, distributed systems, and scaling laws to practical AI constraints.

## Atlas Nodes

`linear_algebra`, `calculus`, `probability`, `statistics`, `information_theory`, `optimization`, `numerical_methods`, `algorithms_data_structures`, `complexity_computability`, `distributed_systems`, `empirical_scaling_laws`

## Prerequisites

Learners should be comfortable with basic algebra and programming. They do not need advanced proof fluency, but they must be willing to inspect shapes, units, and assumptions.

## Core Concepts

- Linear algebra supplies tensors, projections, similarity, and factorization.
- Calculus and automatic differentiation explain how local changes affect loss.
- Probability and statistics explain uncertainty, estimation, sampling, and evaluation.
- Optimization connects objectives to parameter updates.
- Numerical analysis explains why mathematically correct computations can fail in finite precision.
- Algorithms, complexity, distributed systems, and scaling laws determine what is feasible at real size.

## Teaching Plan

1. Start with a simple prediction function: `y_hat = Xw`.
2. Annotate every dimension and verify that the matrix multiplication is legal.
3. Define a loss and derive the gradient in words before symbols.
4. Show a finite-difference check and explain why it catches implementation errors.
5. Discuss how batch size, precision, memory, and distributed execution alter the same math.

## Guided Discussion

- What does a gradient say, and what does it not say?
- Why can a model improve training loss while becoming worse for the intended task?
- Which errors are mathematical, which are statistical, and which are systems errors?
- What changes when the dataset no longer fits in memory?

## Lab

Implement or sketch one training step for linear regression.

Required steps:

1. Define `X`, `y`, `w`, predictions, loss, gradient, and update.
2. Annotate every tensor shape.
3. Add one numerical check, such as finite differences or one-step loss decrease.
4. Write one paragraph explaining what could go wrong numerically.

## Assessment Questions

1. Why does shape checking catch many model bugs before training starts?
2. What is the difference between an objective and an evaluation metric?
3. Why does finite precision matter for optimization?
4. How do scaling laws differ from ordinary benchmark reports?
5. What is one reason distributed training can change system behavior even if the objective is unchanged?

## Deliverable

A short note or code snippet proving the learner can move from objective to gradient to update.

## Mastery Rubric

| Level | Evidence |
|---|---|
| Developing | Can name the math areas but cannot trace a full update. |
| Proficient | Can derive or verify a simple update and identify one numerical risk. |
| Advanced | Can connect the same update to batching, precision, distributed execution, and evaluation. |

## Common Failure Mode

Memorizing formulas without checking shapes, assumptions, units, or numerical behavior.

# AI Mastery Glossary

> *A living glossary of concepts encountered throughout AI Mastery.*

---

# Purpose

The glossary serves as the shared vocabulary of AI Mastery.

Terms are introduced only after they have been studied within the curriculum.

Each entry captures not only a concise definition, but also the engineering significance of the concept and its role within the broader AI stack.

The glossary grows alongside the repository and reflects understanding rather than memorization.

---

# Principles

The glossary is intended to be:

* concise rather than encyclopedic;
* engineering-oriented rather than purely academic;
* connected rather than isolated;
* continuously refined as understanding deepens.

Every concept should help strengthen a coherent mental model of the AI stack rather than exist as an isolated definition.

---

# Entry Structure

Whenever applicable, each glossary entry should include:

* **Definition** — a concise explanation of the concept.
* **Purpose** — why the concept exists and which problem it solves.
* **AI Stack Context** — where the concept fits within the overall AI ecosystem.
* **Related Concepts** — references to closely connected glossary entries.
* **Introduced In** — the module where the concept first appears.

Entries should prioritize conceptual clarity over exhaustive completeness.

---

# Evolution

The glossary evolves together with the curriculum.

Definitions may be refined as new concepts are introduced and existing knowledge becomes more sophisticated.

Earlier entries should remain conceptually consistent while becoming progressively more precise.

Whenever appropriate, entries should reference related concepts to highlight dependencies and relationships across the AI stack.

The glossary should evolve by refining existing knowledge rather than replacing it.

Growth in understanding should be reflected through increased precision, stronger connections between concepts, and deeper engineering insight.

---

# Writing Guidelines

Each entry should:

* remain concise;
* use consistent terminology;
* avoid unnecessary jargon;
* emphasize engineering intuition;
* avoid implementation details unless they are essential to understanding the concept.

Detailed explanations belong in the corresponding modules or dedicated technical documents rather than in the glossary itself.

---

# Scope

The glossary documents concepts encountered throughout AI Mastery, including topics related to:

* mathematics;
* machine learning;
* deep learning;
* AI runtime;
* systems programming;
* compilers;
* inference;
* serving;
* evaluation;
* explainability;
* safety;
* security;
* software engineering.

Only concepts that have been genuinely studied should be added.

Every entry represents knowledge earned through study, implementation, experimentation, and engineering practice.

---

# Entry Template

```md
## Concept

**Definition**

...

**Purpose**

...

**AI Stack Context**

...

**Repository Components**

- ...

**Related Concepts**

- ...

**Introduced In**

Module X.Y — ...
```

--------------------------------------------------------------------------------------------

## Scalar

**Definition**

A tensor with rank 0 representing a single numerical value.

**Purpose**

Represents the simplest possible unit of numerical data.

**AI Stack Context**

Scalars commonly appear as constants, individual tensor elements, loss values, and computed metrics.

**Related Concepts**

* Tensor
* Rank
* Shape

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Vector

**Definition**

A tensor with rank 1 representing an ordered collection of values.

**Purpose**

Represents one-dimensional numerical data.

**AI Stack Context**

Vectors commonly represent feature vectors, embeddings, logits, and model parameters.

**Related Concepts**

* Tensor
* Matrix
* Rank
* Shape

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Matrix

**Definition**

A tensor with rank 2 representing values organized along two independent axes.

**Purpose**

Represents relationships between two dimensions of data.

**AI Stack Context**

Matrices are widely used for linear transformations, attention mechanisms, weight matrices, and matrix multiplication.

**Related Concepts**

* Tensor
* Vector
* Rank
* Shape

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Tensor

**Definition**

A multidimensional numerical object represented by data together with metadata describing how that data should be interpreted.

**Purpose**

Provides a unified abstraction capable of representing many different kinds of numerical data without requiring domain-specific data structures.

**AI Stack Context**

Tensors are the fundamental data abstraction used throughout modern AI frameworks, runtimes, inference engines, and model formats.

**Related Concepts**

* Scalar
* Vector
* Matrix
* Shape
* Rank
* Dtype
* Strides

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Rank

**Definition**

The number of dimensions (axes) of a tensor.

**Purpose**

Describes the structural complexity of a tensor independently of its semantic meaning.

**AI Stack Context**

Rank determines how tensor operations interpret dimensions, indexing, and broadcasting behavior.

**Related Concepts**

* Tensor
* Shape

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Shape

**Definition**

The ordered tuple specifying the size of each dimension of a tensor.

**Purpose**

Describes the logical organization of tensor data.

**AI Stack Context**

Shape is fundamental to tensor operations, model architectures, memory allocation, and runtime validation.

**Related Concepts**

* Tensor
* Rank
* Dtype
* Strides

**Introduced In**

Module 1.1 — Vectors, Matrices and Tensors

---

## Storage

**Definition**

The underlying memory that contains the raw tensor data.

**Purpose**

Provides the physical location where tensor elements are stored independently of how they are interpreted.

**AI Stack Context**

Storage may be shared by multiple tensors exposing different logical views of the same data.

**Related Concepts**

* Tensor
* Shape
* Dtype
* Strides

**Introduced In**

Module 1.2 — Shape, Dtype and Storage

---

## Dtype

**Definition**

Metadata describing how each tensor element is represented and interpreted in memory.

**Purpose**

Determines the size of each element, its numerical representation, and how operations interpret its bytes.

**AI Stack Context**

Choosing an appropriate dtype directly affects memory usage, numerical precision, and computational performance.

**Related Concepts**

* Tensor
* Storage
* Shape
* Strides

**Introduced In**

Module 1.2 — Shape, Dtype and Storage

---

## Strides

**Definition**

Metadata specifying how many elements must be skipped in memory when incrementing an index along each tensor axis.

**Purpose**

Maps logical tensor indices to physical memory locations.

**AI Stack Context**

Strides enable efficient views, transpositions, slicing, and other metadata-only transformations without copying storage.

**Related Concepts**

* Tensor
* Storage
* Shape
* Dtype

**Introduced In**

Module 1.2 — Shape, Dtype and Storage

---

## Contiguous Tensor

**Definition**

A tensor whose elements are laid out in memory according to the default contiguous layout for its shape.

**Purpose**

Represents the standard memory layout from which alternative views can be derived.

**AI Stack Context**

Many tensor operations are most efficient on contiguous tensors, while non-contiguous tensors often arise from views such as transpose or slicing.

**Related Concepts**

* Tensor
* Storage
* Shape
* Strides

**Introduced In**

Module 1.2 — Shape, Dtype and Storage

---

## Offset

**Definition**

The position of a tensor element within its underlying storage.

**Purpose**

Maps logical tensor coordinates to a physical storage location.

**AI Stack Context**

Offsets are computed from tensor indices and strides during runtime.

**Related Concepts**

* Storage
* Strides
* Tensor Indexing

**Introduced In**

Module 1.3 — Tensor Representation and Indexing

---

## Tensor Indexing

**Definition**

The process of accessing tensor elements using logical coordinates.

**Purpose**

Allows runtime systems to retrieve tensor elements independently of their physical memory layout.

**AI Stack Context**

Tensor indexing converts logical indices into storage offsets through stride computation.

**Related Concepts**

* Offset
* Shape
* Strides

**Introduced In**

Module 1.3 — Tensor Representation and Indexing

---

## Bounds Checking

**Definition**

Runtime validation ensuring that every tensor index falls within the valid range of its corresponding dimension.

**Purpose**

Prevents invalid memory accesses and guarantees safe tensor indexing.

**Related Concepts**

* Shape
* Tensor Indexing
* Invariant

**Introduced In**

Module 1.3 — Tensor Representation and Indexing

---

## Invariant

**Definition**

A property that must always hold for a valid runtime object.

**Purpose**

Defines the conditions required for an object to remain internally consistent throughout its lifetime.

**AI Stack Context**

Tensor invariants simplify runtime implementation by guaranteeing properties such as rank consistency and storage validity after construction.

**Related Concepts**

* Tensor
* Shape
* Storage

**Introduced In**

Module 1.3 — Tensor Representation and Indexing

---

## View

**Definition**

A tensor that shares the same storage as another tensor while exposing different metadata.

**Purpose**

Allows multiple logical representations of the same physical memory without copying data.

**Related Concepts**

* Storage
* Shape
* Strides
* Memory Aliasing

**Introduced In**

Module 1.4 — Views, Reshape and Transpose

---

## Memory Aliasing

**Definition**

The condition in which multiple tensors reference the same storage.

**Purpose**

Explains why modifications performed through one tensor are immediately visible from every other view sharing that storage.

**Related Concepts**

* View
* Storage

**Introduced In**

Module 1.4 — Views, Reshape and Transpose

---

## Metadata-Only Transformation

**Definition**

A tensor operation implemented exclusively by modifying metadata, without copying the underlying storage.

**Purpose**

Improves runtime efficiency by avoiding unnecessary memory movement.

**Related Concepts**

* View
* Shape
* Strides
* Transpose

**Introduced In**

Module 1.4 — Views, Reshape and Transpose

---

## Contiguous Tensor

**Definition**

A tensor whose logical traversal follows the physical order of elements in storage.

**Purpose**

Determines whether certain operations, such as reshape, can be implemented as metadata-only transformations.

**Related Concepts**

* Storage
* Strides
* Reshape

**Introduced In**

Module 1.4 — Views, Reshape and Transpose

---

## Logical Layout

**Definition**

The interpretation of storage defined by a tensor's metadata, including its shape and strides.

**Purpose**

Separates the physical organization of memory from the logical structure exposed by the tensor.

**AI Stack Context**

Multiple tensors may expose different logical layouts while sharing the same storage.

**Related Concepts**

* Tensor
* Storage
* Shape
* Strides
* View

**Introduced In**

Module 1.4 — Views, Reshape and Transpose
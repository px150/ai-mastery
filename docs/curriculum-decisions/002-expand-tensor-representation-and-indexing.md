# Roadmap Change Record #02

## Observation

During the implementation of the first tensor abstraction, it became evident that memory layout, stride computation, indexing, and tensor invariants cannot be meaningfully separated into independent learning units.

Implementing contiguous strides naturally led to offset computation, which in turn required scalar indexing and constructor invariants.

These concepts form a single architectural layer describing how a runtime represents and accesses tensor data.

## Proposal

Replace:

- Module 1.3 — Memory Layout and Strides
- Module 1.4 — Broadcasting

with:

- Module 1.3 — Tensor Representation and Indexing
- Module 1.4 — Views, Reshape and Transpose
- Module 1.5 — Broadcasting

## Motivation

The original roadmap underestimated the amount of engineering knowledge required before broadcasting could be introduced.

Understanding broadcasting requires a solid understanding of:

- contiguous memory layout;
- stride computation;
- offset computation;
- tensor indexing;
- metadata-only transformations;
- storage sharing.

Grouping tensor representation and indexing into a single module creates a much more natural progression from theory to implementation.

Broadcasting then becomes a consequence of the underlying tensor model rather than an isolated feature.

## Impact

Phase 1 becomes slightly longer but conceptually stronger.

The implementation now mirrors the natural evolution followed by real tensor runtimes:

Tensor representation

↓

Tensor indexing

↓

Views and metadata transformations

↓

Broadcasting

This improves continuity between the conceptual model, the implementation, and later runtime topics such as PyTorch, ONNX Runtime, TensorRT, and vLLM.
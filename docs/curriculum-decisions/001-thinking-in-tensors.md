# Curriculum Decision Record #001

**Status:** Accepted

**Date:** 2026-06-28

---

## Observation

During the transition from the AI Ecosystem modules to the Tensor modules, it became apparent that the curriculum assumed an engineering intuition that had not yet been established.

Most learners initially interpret a tensor as "just a multidimensional array", making it difficult to later understand concepts such as shape, dtype, strides, memory layout, dispatch, and the tensor abstractions used throughout modern AI frameworks and runtimes.

---

## Proposal

Introduce a new module immediately before Phase 1.

**Module 0.5 — Thinking in Tensors**

This module focuses on the engineering intuition behind tensors before introducing their mathematical definition or implementation.

---

## Motivation

The primary objective of the module is to answer the question:

> **Why do tensors exist?**

before answering:

> **What is a tensor?**

By approaching tensors as an engineering abstraction rather than a mathematical object, the learner develops a mental model that naturally supports the subsequent study of PyTorch, ONNX Runtime, GPU execution, and modern AI infrastructure.

---

## Impact

- The overall roadmap structure remains unchanged.
- No existing modules are modified or removed.
- Phase 1 begins with a stronger conceptual foundation.
- Tensor-related concepts are introduced progressively rather than all at once.
- Future discussions about memory layout, dispatch, runtimes, GPU kernels, and compiler optimizations become significantly more intuitive.

---

## Decision

The proposal is accepted.

Module **0.5 — Thinking in Tensors** is officially added to the curriculum and becomes the bridge between the AI Ecosystem overview and the Tensor Core modules.

This change is considered a curriculum improvement rather than a roadmap restructuring.

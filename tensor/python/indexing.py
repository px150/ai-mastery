def compute_offset(
    indices: tuple[int, ...],
    shape: tuple[int, ...],
    strides: tuple[int, ...],
) -> int:
    indices_rank = len(indices)
    shape_rank = len(shape)

    if indices_rank != shape_rank:
        raise ValueError(
            f"Indices rank ({indices_rank}) does not match shape rank ({shape_rank})."
        )

    for idx, dim in zip(indices, shape):
        if idx < 0 or idx >= dim:
            raise IndexError(f"Index {idx} is out of bounds for dimension size {dim}.")

    return sum(idx * stride for idx, stride in zip(indices, strides))

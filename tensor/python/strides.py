def compute_contiguous_strides(
    shape: tuple[int, ...],
) -> tuple[int, ...]:
    """
    Computes the strides for a contiguous row-major tensor.

    The returned strides indicate how many storage elements must be skipped to
    advance by one position along each dimension. The last dimension always has
    stride 1, and each preceding stride is the product of the sizes of all
    trailing dimensions.

    Examples:
        ()            -> ()
        (5,)          -> (1,)
        (2, 3)        -> (3, 1)
        (2, 3, 4)     -> (12, 4, 1)
    """
    strides: list[int] = []
    current_stride = 1

    for dim in reversed(shape):
        strides.append(current_stride)
        current_stride *= dim

    return tuple(reversed(strides))
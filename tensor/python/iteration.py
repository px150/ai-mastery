def iterate_indices(shape: tuple[int, ...]):
    if shape == ():
        yield ()
        return

    def visit(axis: int, prefix: tuple[int, ...]):
        if axis == len(shape):
            yield prefix
            return

        for index in range(shape[axis]):
            yield from visit(axis + 1, prefix + (index,))

    yield from visit(0, ())

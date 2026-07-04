from python.strides import compute_contiguous_strides


def test_scalar():
    assert compute_contiguous_strides(()) == ()


def test_vector():
    assert compute_contiguous_strides((5,)) == (1,)


def test_matrix():
    assert compute_contiguous_strides((2, 3)) == (3, 1)


def test_rank_3():
    assert compute_contiguous_strides((2, 3, 4)) == (12, 4, 1)


def test_rank_4():
    assert compute_contiguous_strides((2, 3, 4, 5)) == (60, 20, 5, 1)

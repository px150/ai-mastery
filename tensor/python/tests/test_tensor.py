from python.tensor import Tensor
from python.storage import Storage
from python.dtype import DType


def make_matrix():
    return Tensor(
        storage=Storage(data=[1, 2, 3, 4, 5, 6]),
        dtype=DType.FLOAT32,
        shape=(2, 3),
    )


# Transpose


def test_transpose_returns_new_tensor():
    x = make_matrix()
    y = x.transpose()

    assert x is not y


def test_transpose_shares_storage():
    x = make_matrix()
    y = x.transpose()

    assert x.storage is y.storage


def test_transpose_preserves_dtype():
    x = make_matrix()
    y = x.transpose()

    assert x.dtype == y.dtype


def test_transpose_swaps_shape():
    x = make_matrix()
    y = x.transpose()

    assert y.shape == (3, 2)


def test_transpose_swaps_strides():
    x = make_matrix()
    y = x.transpose()

    assert y.strides == (1, 3)


def test_transpose_does_not_mutate_original_tensor():
    x = make_matrix()
    y = x.transpose()

    assert x.shape == (2, 3)
    assert x.strides == (3, 1)


def test_transposed_tensor_indexes_correctly():
    x = make_matrix()
    y = x.transpose()

    assert y[0, 0] == 1
    assert y[0, 1] == 4
    assert y[1, 0] == 2
    assert y[1, 1] == 5
    assert y[2, 0] == 3
    assert y[2, 1] == 6


# Contiguity


def test_contiguity_new_tensor():
    x = make_matrix()
    assert x.is_contiguous()


def test_contiguity_tensor_not_contiguous_after_transpose():
    x = make_matrix()
    y = x.transpose()
    assert not y.is_contiguous()


def test_contiguity_tensor_contiguous_after_double_transpose():
    x = make_matrix()
    y = x.transpose().transpose()
    assert y.is_contiguous()
    assert y.shape == x.shape
    assert y.strides == x.strides


def test_contiguity_vector_always_contiguous():
    x = Tensor(
        storage=Storage(
            data=[
                1,
                2,
                3,
                4,
                5,
            ]
        ),
        dtype=DType.FLOAT32,
        shape=(5,),
    )
    assert x.is_contiguous()

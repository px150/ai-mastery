from python.tensor import Tensor
from python.storage import Storage
from python.dtype import DType

import pytest


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


# Reshape


def test_reshape_preserves_storage():
    storage = Storage([1, 2, 3, 4, 5, 6])
    tensor = Tensor(storage=storage, dtype=DType.FLOAT32, shape=(2, 3))

    reshaped = tensor.reshape((3, 2))

    assert reshaped.storage is tensor.storage
    assert reshaped.shape == (3, 2)
    assert reshaped.strides == (2, 1)


def test_reshape_preserves_logical_order_for_contiguous_tensor():
    storage = Storage([1, 2, 3, 4, 5, 6])
    tensor = Tensor(storage=storage, dtype=DType.FLOAT32, shape=(2, 3))

    reshaped = tensor.reshape((3, 2))

    assert reshaped[(0, 0)] == 1
    assert reshaped[(0, 1)] == 2
    assert reshaped[(1, 0)] == 3
    assert reshaped[(1, 1)] == 4
    assert reshaped[(2, 0)] == 5
    assert reshaped[(2, 1)] == 6


def test_reshape_rejects_different_number_of_elements():
    storage = Storage([1, 2, 3, 4, 5, 6])
    tensor = Tensor(storage=storage, dtype=DType.FLOAT32, shape=(2, 3))

    with pytest.raises(ValueError):
        tensor.reshape((4, 2))


def test_contiguous_returns_self_when_tensor_is_already_contiguous():
    x = make_matrix()

    y = x.contiguous()

    assert y is x


def test_contiguous_materializes_non_contiguous_tensor():
    x = make_matrix()
    y = x.transpose()

    z = y.contiguous()

    assert z is not y
    assert z.storage is not y.storage
    assert z.shape == y.shape
    assert z.strides == (2, 1)
    assert z.is_contiguous()


def test_contiguous_preserves_logical_order():
    x = make_matrix()
    y = x.transpose()

    z = y.contiguous()

    assert z[(0, 0)] == 1
    assert z[(0, 1)] == 4
    assert z[(1, 0)] == 2
    assert z[(1, 1)] == 5
    assert z[(2, 0)] == 3
    assert z[(2, 1)] == 6


def test_reshape_materializes_non_contiguous_tensor():
    x = make_matrix()
    y = x.transpose()

    z = y.reshape((6,))

    assert z.storage is not y.storage
    assert z.shape == (6,)
    assert z.strides == (1,)
    assert z.is_contiguous()

    assert z[(0,)] == 1
    assert z[(1,)] == 4
    assert z[(2,)] == 2
    assert z[(3,)] == 5
    assert z[(4,)] == 3
    assert z[(5,)] == 6

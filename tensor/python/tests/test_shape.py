import pytest

from python.tensor import Tensor
from python.storage import Storage
from python.dtype import DType


def test_shape_and_strides_must_have_same_rank():
    with pytest.raises(ValueError):
        Tensor(
            storage=Storage([1, 2, 3, 4, 5, 6]),
            dtype=DType.FLOAT32,
            shape=(2, 3),
            strides=(3,),
        )


def test_storage_must_be_large_enough():
    with pytest.raises(ValueError):
        Tensor(
            storage=Storage([1, 2, 3]),
            dtype=DType.FLOAT32,
            shape=(2, 3),
        )

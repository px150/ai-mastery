from dataclasses import dataclass

from .storage import Storage
from .dtype import DType

from .strides import compute_contiguous_strides
from .shape import compute_tensor_size
from .indexing import compute_offset


@dataclass
class Tensor:
    storage: Storage
    dtype: DType
    shape: tuple[int, ...]
    strides: tuple[int, ...] | None = None

    def __post_init__(self):
        needed_tensor_size = compute_tensor_size(self.shape)
        storage_size = len(self.storage)

        if needed_tensor_size > storage_size:
            raise ValueError(
                f"Tensor requires {needed_tensor_size} elements but storage contains only {storage_size}."
            )

        if self.strides is None:
            self.strides = compute_contiguous_strides(self.shape)

        if len(self.shape) != len(self.strides):
            raise ValueError(
                f"Shape rank ({len(self.shape)}) does not match "
                f"strides rank ({len(self.strides)})."
            )

    def __getitem__(self, indices: tuple[int, ...]):
        assert self.strides is not None

        offset = compute_offset(indices, self.shape, self.strides)
        return self.storage[offset]

    def transpose(self) -> "Tensor":
        if len(self.shape) != 2:
            raise ValueError("Transpose currently supports only rank-2 tensors.")

        assert self.strides is not None

        return Tensor(
            storage=self.storage,
            dtype=self.dtype,
            shape=(self.shape[1], self.shape[0]),
            strides=(self.strides[1], self.strides[0]),
        )

    def is_contiguous(self) -> bool:
        assert self.strides is not None
        return self.strides == compute_contiguous_strides(self.shape)

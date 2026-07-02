from dataclasses import dataclass

from .storage import Storage
from .dtype import DType

@dataclass
class Tensor:
    storage: Storage
    dtype: DType
    shape: tuple[int, ...]
    strides: tuple[int, ...] | None = None
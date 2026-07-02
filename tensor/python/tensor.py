from dataclasses import dataclass

from .storage import Storage
from .dtype import DType

from .strides import compute_contiguous_strides

@dataclass
class Tensor:
	storage: Storage
	dtype: DType
	shape: tuple[int, ...]
	strides: tuple[int, ...] | None = None

	def __post_init__(self):
		if self.strides is None:
			self.strides = compute_contiguous_strides(self.shape)
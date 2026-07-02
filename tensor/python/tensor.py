from dataclasses import dataclass

from .storage import Storage
from .dtype import DType

from .strides import compute_contiguous_strides
from .shape import compute_tensor_size

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
		
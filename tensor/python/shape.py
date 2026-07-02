import math

def compute_tensor_size(shape: tuple[int, ...]) -> int:
	return math.prod(shape)
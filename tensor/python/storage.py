from dataclasses import dataclass
from numbers import Number

@dataclass
class Storage:
    data: list[Number]
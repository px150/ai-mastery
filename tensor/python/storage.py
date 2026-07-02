from dataclasses import dataclass
from numbers import Number


@dataclass
class Storage:
    data: list[Number]

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int):
        return self.data[index]

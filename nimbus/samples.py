import numpy.typing as npt
from dataclasses import dataclass, replace


@dataclass
class Samples:
    """Samples is a data class that keeps samples and their
    metadata together between Pipeline stages"""

    data: npt.NDArray
    sample_rate: int = 0

    def replace(self, **changes):
        return replace(self, **changes)

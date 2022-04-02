import numpy.typing as npt
from dataclasses import dataclass, replace


@dataclass
class Samples:
    """
    Samples is a data class that keeps samples and their
    metadata together between Pipeline stages

    Attributes
    ----------
    data: npt.NDArray
        Data
    sample_rate: int
        Sample rate

    """

    data: npt.NDArray
    sample_rate: int = 0

    def replace(self, **changes):
        """
        Replaces either data or sample_rate and returns new Samples object
        """
        return replace(self, **changes)

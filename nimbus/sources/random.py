import numpy as np
import numpy.typing as npt
from nimbus import Samples


class Random:
    """
    Random is a source class that generates a random signal

    Notes
    -----
        This class is only used for testing purposes

    Attributes
    ----------
    size: int
        Size of data to create

    """

    def __init__(self, size: int):
        """
        Parameters
        ----------
        size: int
            Size of data to create
        """
        self.size = size

    def generate(self) -> npt.NDArray:
        """
        Generates a random, uniform signal
        Returns
        -------
        Samples
            Samples data class object

        """
        return Samples(data=np.random.rand(self.size))

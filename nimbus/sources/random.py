import numpy as np
import numpy.typing as npt


class Random:
    """Random is a source that generates a random signal"""

    def __init__(self, size: int):
        self.size = size

    def generate(self):
        """Generates a random, uniform signal

        Parameters:
            signal (npt.NDArray): The randomly generated signal"""

        return np.random.rand(self.size)

import numpy as np
import numpy.typing as npt


class Gain:
    """Gain is a transformer that applies a gain to a signal"""

    def __init__(self, gain: float):
        """Constructs a new Gain transformer with a gain of gain

        Parameters:
            gain (float): The gain of the transformer
        """
        self.gain = gain

    def execute(self, signal: npt.NDArray) -> npt.NDArray:
        """Applies a gain to the input

        Parameters:
            signal (npt.NDArray): The signal to gain
        """
        return signal * self.gain

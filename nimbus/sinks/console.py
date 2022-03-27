import numpy.typing as npt
from nimbus import Samples
import numpy as np


class Console:
    """Console is a sink that prints a signal to the console"""

    def __init__(self):
        pass

    def execute(self, signal: Samples):
        """Prints signal to console"""
        print(signal.data)
        return

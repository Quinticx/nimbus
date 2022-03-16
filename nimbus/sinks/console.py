import numpy.typing as npt


class Console:
    """Console is a sink that prints a signal to the console"""

    def __init__(self):
        pass

    def console_print(self, signal: npt.NDArray):
        """Prints signal to console"""
        print(signal)
        return 

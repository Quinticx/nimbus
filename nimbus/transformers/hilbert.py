import numpy as np
import numpy.typing as npt
import scipy.signal as sp


class Hilbert:
    """Hilbert is a transformer that applies a Hilbert transform on a signal to perform AM demodulation"""

    def __init__(self):
        """Constructs a new Hilbert transformer with a signal"""
        pass

    def execute(self, signal: npt.NDArray) -> npt.NDArray:
        """Performs Hilbert transform on signal

        Parameters:
            signal (npt.NDArray): The signal to transform
        """
        analytic_signal = sp.hilbert(signal)
        amp_envelope = np.abs(analytic_signal)
        return amp_envelope

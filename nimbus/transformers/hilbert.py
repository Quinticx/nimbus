import numpy as np
import scipy.signal as sp
from nimbus import Samples


class Hilbert:
    """
    Hilbert is a transformer class that applies a Hilbert transform
    on a signal to perform AM demodulation

    """

    def __init__(self):
        """
        Constructs a new Hilbert transformer with a signal
        """
        pass

    def execute(self, signal: Samples) -> Samples:
        """
        Performs Hilbert transform on signal

        Parameters
        ----------
        signal: Samples
            The signal to transform

        Returns
        -------
        signal: Samples
            Returns signal.data with envelope of Hilbert transform
        """
        analytic_signal = sp.hilbert(signal.data)
        amp_envelope = (np.abs(analytic_signal) - 0.5) * 2
        return signal.replace(data=amp_envelope)

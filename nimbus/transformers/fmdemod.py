from nimbus import Samples
import numpy as np


class FM_Demod:
    """
    FM_Demod is a transformer class that takes in a signal and fm demodulates it.
    """

    def __init__(self):
        """
        Constructs new FM_Demod Transformer
        """
        pass

    def execute(self, signal: Samples) -> Samples:
        """
        Performs FM Demodulation by taking phase difference between adjacent samples

        Parameters
        ----------
        signal: Samples
            The signal to transform

        Raises
        ------
        ValueError
            Signal is not of type complex 64

        Returns
        -------
        signal: Sample
            Replaces signal.data with FM demodulated signal
        """
        if not signal.data.dtype == np.complex64:
            raise ValueError(
                f"FM Demod Transformer requires np.complex64 signal: {signal.data.dtype}"
            )

        sample = np.diff((np.unwrap(np.angle(signal.data))) / (2 * np.pi))
        return signal.replace(data=sample)

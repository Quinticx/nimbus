from nimbus import Samples
import numpy as np


class FM_Demod:
    def __init__(self):
        pass

    def execute(self, signal: Samples) -> Samples:
        """Performs FM Demodulation by taking phase difference between adjacent samples

        Parameters:
            signal (Samples): The signal to transform
        """
        sample = np.diff((np.unwrap(np.angle(signal.data))) / (2 * np.pi))
        return signal.replace(data=sample)

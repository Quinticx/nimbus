from rtlsdr import RtlSdr
from nimbus import Samples
import numpy.typing as npt
import numpy as np


class SDR:
    """
    SDR is a source class that reads from an SDR connected to the computer and streams the output.

    Attributes
    ----------
    sample_rate: int
        Sample rate of the SDR

    frequency: int
        Frequency SDR is to be tuned to.


    """

    def __init__(self, sample_rate: int, frequency: int):
        """
        Constructs new SDR Source
        Parameters
        ----------
        sample_rate: int
            Sample rate of the SDR

        frequency: int
            Frequency the SDR is tuned to
        """
        self.sdr = RtlSdr()
        self.sdr.sample_rate = sample_rate
        self.sdr.center_freq = frequency
        self.sdr.freq_correction = 60
        self.sdr.gain = "auto"

    def read(self) -> npt.NDArray:
        """
        Reads from SDR and returns to stream of type Samples

        Returns
        -------
        Samples
            New Samples data class object where data is samples and sample_rate is sample rate
        """
        num_samp = 2048
        samples = np.array(self.sdr.read_samples(num_samp))
        return Samples(data=samples, sample_rate=int(self.sdr.sample_rate))

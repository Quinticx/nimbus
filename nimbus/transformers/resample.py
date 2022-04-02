import scipy.signal as sp
from nimbus import Samples


class Resample:
    """
    Reample is a transformer class that resamples the input at a new rate

    Attributes
    ----------
    sample_rate: int
        New samples rate

    """

    def __init__(self, sample_rate: int):
        """
        Constructs a new Resample transformer

        Parameters
        ----------
        sample_rate: int
            New sample rate
        """
        self.sample_rate = sample_rate

    def execute(self, signal: Samples) -> Samples:
        """
        Resamples signal to new sampling rate

        Parameters
        ----------
        signal: Samples
            Returns new Sample object where signal is resampled signal and sample_rate is the new sample rate
        """
        num_samp = int((self.sample_rate / signal.sample_rate) * len(signal.data))
        new_signal = sp.resample(signal.data, num_samp)
        return Samples(new_signal.astype(signal.data.dtype), self.sample_rate)

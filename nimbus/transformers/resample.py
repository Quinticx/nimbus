import scipy.signal as sp
import numpy as np
import numpy.typing as npt
from nimbus import Samples


class Resample:
    def __init__(self, sample_rate: int):
        self.sample_rate = sample_rate

    def execute(self, signal: Samples) -> Samples:
        num_samp = int((self.sample_rate / signal.sample_rate) * len(signal.data))
        new_signal = sp.resample(signal.data, num_samp)
        return Samples(new_signal, self.sample_rate)

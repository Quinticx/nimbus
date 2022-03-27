from rtlsdr import RtlSdr
from nimbus import Samples
import numpy as np

class SDR:
    ''' SDR is a source that reads from an SDR connected to the computer'''

    def __init__(self, sample_rate: int, frequency: int):
        self.sdr = RtlSdr()
        self.sdr.sample_rate = sample_rate
        self.sdr.center_freq = frequency
        self.sdr.freq_correction = 60
        self.sdr.gain = 'auto'

    def read(self):
        num_samp = 2048
        samples = np.array(self.sdr.read_samples(num_samp))
        return Samples(data=samples, sample_rate = int(self.sdr.sample_rate))

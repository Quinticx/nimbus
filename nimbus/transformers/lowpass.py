import numpy as np
from nimbus import Samples
import scipy.signal as ss

class LowPass:


    def __init__(self):
        
        pass

    def execute(self, signal: Samples) -> Samples:
        N = 3
        Wn = 5000
        b, a = ss.butter(N, Wn, btype='lp', output='ba', fs=signal.sample_rate)
        zi = ss.lfilter_zi(b, a)
        z, _ = ss.lfilter(b, a, signal.data, zi=zi*signal.data[0])
        z = np.abs(z)

        return signal.replace(data=z.astype(np.int16))

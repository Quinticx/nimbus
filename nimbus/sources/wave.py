import numpy as np
import numpy.typing as npt
from scipy.io import wavfile

class Wave:
    '''Wave is a source that reads from a wave file (.wav) and returns the signal'''

    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        '''Read .wav file and return signal'''
        frame_rate, data = wavfile.read(self.filename)
        signal = np.frombuffer(data, dtype="int16")
        return signal, frame_rate
        

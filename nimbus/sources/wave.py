import numpy as np
import wave
import pathlib
from nimbus import Samples


class Wave:
    """Wave is a source that reads from a wave file (.wav)
    and returns the signal"""

    def __init__(self, filename: pathlib.Path, buffer_size: int = 128):
        self.wavefile = wave.open(str(filename))
        self.buffer_size = buffer_size
        self.sample_rate = self.wavefile.getframerate()

    def read(self):
        """Read .wav file and return signal"""
        data = self.wavefile.readframes(self.buffer_size)
        if not data:
            raise EOFError()
        data = np.frombuffer(data, dtype="int16")
        return Samples(data=data, sample_rate=self.sample_rate)

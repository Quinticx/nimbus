import numpy as np
import numpy.typing as npt
import wave
import pathlib

class Wave:
    """Wave is a source that reads from a wave file (.wav) and returns the signal"""

    def __init__(self, filename: pathlib.Path, buffer_size: int=128):
        self.wavefile = wave.open(str(filename))
        self.buffer_size = buffer_size

    def read(self):
        """Read .wav file and return signal"""
        data = self.wavefile.readframes(self.buffer_size)
        if not data:
            raise IndexError()
        data = np.frombuffer(data, dtype="int16")
        return data

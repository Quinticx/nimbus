import numpy.typing as npt
import numpy as np
import wave
from nimbus import Samples


class Wave:
    """Wave is a sink that saves a signal to a wave file"""

    def __init__(self, filename: str = "output.wav"):
        self.filename = filename
        self.wavefile = wave.open(str(filename), "w")
        self.wavefile.setnchannels(1)
        self.wavefile.setsampwidth(2)

    def execute(self, signal: Samples):
        """Writes signal to .wav file"""
        try:
            self.wavefile.setframerate(signal.sample_rate)
        except wave.Error:
            pass
        bytez = signal.data.tobytes()
        self.wavefile.writeframes(bytez)

    def close(self):
        self.wavefile.close()

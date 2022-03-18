import scipy.io.wavfile as spwave
import numpy.typing as npt
import numpy as np

class Wave:
    """Wave is a sink that saves a signal to a wave file"""

    def __init__(self, filename: str = "output.wav", frame_rate: int = 22050):
        self.filename = filename
        self.frame_rate = frame_rate

    def write(self, signal: npt.NDArray):
        """Writes signal to .wav file"""
        spwave.write("output.wav", self.frame_rate, signal.astype(np.int16))
        return

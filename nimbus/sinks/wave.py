import wave
from nimbus import Samples
import numpy as np


class Wave:
    """
    Wave is a sink class that saves a signal to a .wav file

    Attributes
    ----------
    filename: str
        Filename to save .wav file as

    """

    def __init__(self, filename: str = "output.wav"):
        """
        Constructs new Wave Sink
        Parameters
        ----------
        filename: str
            Filename to save .wav file as
        """
        self.filename = filename
        self.wavefile = wave.open(str(filename), "w")
        self.wavefile.setnchannels(1)
        self.wavefile.setsampwidth(2)

    def execute(self, signal: Samples):
        """
        Writes signal to .wav file

        Parameters
        ----------
        signal: Samples
            Input signal to save to .wav file

        Raises
        ------
        ValueError
            Signal is not of type int16
        """
        if not signal.data.dtype == np.int16:
            raise ValueError(f"Wave Sink requires int16 signal: {signal.data.dtype}")
        try:
            self.wavefile.setframerate(signal.sample_rate)
        except wave.Error:
            pass
        bytez = signal.data.tobytes()
        self.wavefile.writeframes(bytez)

    def close(self):
        """
        Closes .wav file
        """
        self.wavefile.close()

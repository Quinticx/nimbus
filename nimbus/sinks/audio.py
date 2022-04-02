import pyaudio
import numpy as np
from nimbus import Samples


class Audio:
    """
    Audio is a sink class that plays a .wav file.

    """

    def __init__(self):
        """
        Constructs a new Audio Sink
        """
        self.stream = None

    def execute(self, signal: Samples):
        """
        Parameters
        ----------
        signal: Samples
            Input signal to play aloud

        Raises
        ------
        ValueError
            Signal is not of type float 32

        """
        if not signal.data.dtype == np.float32:
            raise ValueError(
                f"Audio Sink requires np.float32 signal: {signal.data.dtype}"
            )

        if self.stream is None:
            p = pyaudio.PyAudio()
            self.stream = p.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=signal.sample_rate,
                output=True,
            )
        data = signal.data.astype(np.float32).tostring()
        self.stream.write(data)

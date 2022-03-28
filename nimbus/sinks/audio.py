import pyaudio
import numpy as np
from nimbus import Samples


class Audio:
    """Audio is a sink that plays a wave file"""

    def __init__(self):
        self.stream = None

    def execute(self, signal: Samples):
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

import pyaudio
import wave
from nimbus import Samples


class Audio:
    """Audio is a sink that plays a wave file"""

    def __init__(self):
        self.stream = None

    def execute(self, signal: Samples):
        if self.stream == None:
            p = pyaudio.PyAudio()
            self.stream = p.open(
                format=pyaudio.paInt16, channels=1, rate=signal.sample_rate, output=True
            )
        self.stream.write(signal.data.tobytes())

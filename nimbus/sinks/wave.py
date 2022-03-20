import numpy.typing as npt
import numpy as np
import wave


class Wave:
    """Wave is a sink that saves a signal to a wave file"""

    def __init__(self, filename: str = "output.wav", frame_rate: int = 44100):
        self.filename = filename
        self.wavefile = wave.open(str(filename), "w")
        self.wavefile.setnchannels(1)
        self.wavefile.setframerate(frame_rate)
        self.wavefile.setsampwidth(2)

    def execute(self, signal: npt.NDArray):
        """Writes signal to .wav file"""
        signal = signal.tobytes()
        self.wavefile.writeframes(signal)

    def close(self):
        self.wavefile.close()

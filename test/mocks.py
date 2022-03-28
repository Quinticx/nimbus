import numpy as np
import numpy.typing as npt
from nimbus import Samples


class MockSource:
    def __init__(self, signal: npt.NDArray, buffer_size: int = 5, sample_rate: int = 0):
        self.signal = np.array_split(signal, len(signal) // buffer_size)
        self.index = 0
        self.sample_rate = sample_rate

    def read(self):
        self.index += 1
        if self.index > len(self.signal):
            raise EOFError()
        return Samples(data=self.signal[self.index - 1], sample_rate=self.sample_rate)


class MockSink:
    def __init__(self):
        self.buffer = []

    def execute(self, signal: Samples):
        self.buffer.append(signal.data)

    def get_buffer(self):
        return np.concatenate(self.buffer)

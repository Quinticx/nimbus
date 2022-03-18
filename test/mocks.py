import numpy as np
import numpy.typing as npt


class MockSource:
    def __init__(self, signal: npt.NDArray, buffer_size: int = 5):
        self.signal = np.array_split(signal, len(signal) // buffer_size)
        self.index = 0

    def read(self):
        self.index += 1
        return self.signal[self.index - 1]


class MockSink:
    def __init__(self):
        self.buffer = []

    def execute(self, signal: npt.NDArray):
        self.buffer.append(signal)

    def get_buffer(self):
        return np.concatenate(self.buffer)

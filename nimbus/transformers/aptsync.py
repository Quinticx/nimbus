import numpy as np
import numpy.typing as npt
import scipy.signal as sp
from nimbus import Samples


class Apt_Sync:
    """Apt_Sync is a transformer that calculates the cross correlation between a signal and the APT Sync frame"""

    def __init__(self, sync_frame: npt.NDArray):
        """Constructs a new Apt_Sync transformer"""
        self.previous = np.array([])
        self.sync_frame = sync_frame

    def execute(self, signal: Samples) -> Samples:
        samples = signal.data
        index = find_sync_frame(samples, self.sync_frame)
        current = samples[: index + 1]
        next_prev = samples[index:]
        line = np.concatenate((self.previous, current))
        self.previous = next_prev
        return signal.replace(data=line)


def find_sync_frame(signal: npt.NDArray, sync_frame: npt.NDArray) -> int:
    correlation = sp.correlate(signal, sync_frame)
    index = np.argmax(correlation) - len(sync_frame)
    # raise IndexError("No sync frame found!")
    return index

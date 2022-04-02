import numpy as np
import scipy.signal as sp
from nimbus import Samples
import numpy.typing as npt


class Apt_Sync:
    """
    Apt_Sync is a transformer class that calculates the cross correlation between a signal and the APT Sync frame

    Attributes
    ----------
    sync_frame: npt.NDArray
        Sync frame for signal to be correlated against

    """

    def __init__(self, sync_frame: npt.NDArray):
        """
        Constructs a new Apt_Sync transformer

        Parameters
        ----------
        sync_frame: npt.NDArray
            Sync frame for signal to be correlated against

        """
        self.previous = np.array([])
        self.sync_frame = sync_frame

    def execute(self, signal: Samples) -> Samples:
        """
        Syncs image buffers so sync frame is always start of row in image.

        Parameters
        ----------
        signal: Samples
            Input signal to be correlated against sync frame

        Returns
        -------
        signal: Samples
            Returns signal.data which is new image row starting with sync frame

        Raises
        ------
        ValueError
            If signal is not of type float32 or float64

        """
        if not signal.data.dtype in [np.float32, np.float64]:
            raise ValueError(
                f"Apt_Sync Transformer requires np.float32 or np.float64 signal: {signal.data.dtype}"
            )
        samples = signal.data
        index = find_sync_frame(samples, self.sync_frame)
        current = samples[: index + 1]
        next_prev = samples[index:]
        line = np.concatenate((self.previous, current))
        self.previous = next_prev
        return signal.replace(data=line)


def find_sync_frame(signal: npt.NDArray, sync_frame: npt.NDArray) -> int:
    """
    Performs correlation between signal and sync frame to determine where sync is in image row. Once found, it starts the row with the sync frame.

    Parameters
    ----------
    signal: npt.NDArray
        Input singal
    sync_frame: npt.NDArray
        Sync frame

    Returns
    -------
    index: int
        Index of start of sync frame

    """
    correlation = sp.correlate(signal, sync_frame)
    index = np.argmax(correlation) - len(sync_frame)
    # raise IndexError("No sync frame found!")
    return index

import numpy as np
import numpy.typing as npt
import wave
import pathlib
from nimbus import Samples


class Wave:
    """
    Wave is a source that reads from a wave file (.wav) and returns the signal

    Attributes
    ----------
    filename: pathlib.Path
        Path of .wav file to open

    buffer_size: int
        Buffer rate of .wav file


    """

    def __init__(self, filename: pathlib.Path, buffer_size: int = 128):
        """
        Constructs a new Wave Source
        Parameters
        ----------
        filename: pathlib.Path
            Path of .wav file to open

        buffer_size: int
            Buffer rate of .wav file

        """
        self.wavefile = wave.open(str(filename))
        self.buffer_size = buffer_size
        self.sample_rate = self.wavefile.getframerate()

    def read(self) -> npt.NDArray:
        """
        Read .wav file and return signal

        Returns
        -------
        Samples
            New Samples data class object where data is data and sample_rate is sample_rate

        Raises
        ------
        EOFError
            Reached end of file

        """
        data = self.wavefile.readframes(self.buffer_size)
        if not data:
            raise EOFError()
        data = np.frombuffer(data, dtype="int16")
        return Samples(data=data, sample_rate=self.sample_rate)

import numpy as np
import numpy.typing as npt
from nimbus import Samples
import pathlib
import json


class IQ:
    """
    IQ is a source class that reads from an .iq file and returns a numpy array

    Attributes
    ----------
    filename: pathlib.Path
        Path of .iq file to open

    buffer_size: int
        Buffer rate of .iq file

    """

    def __init__(self, filename: pathlib.Path, buffer_size: int = 2048):
        """
        Constructs new IQ Source
        Parameters
        ----------
        filename: pathlib.Path
            Path of .iq file to open

        buffer_size: int
            Buffer size of .iq file


        """
        self.filename = filename
        self.iqfile = open(self.filename, "rb")
        self.buffer_size = buffer_size
        jsonfile = open(filename.with_suffix(".json"), "r")
        info = json.load(jsonfile)
        self.sample_rate = info["sample_rate"]

    def read(self) -> npt.NDArray:
        """
        Read .iq file and return signal

        Returns
        -------
        Samples
            New Samples data class object where data is data and sample_rate is sample_rate

        Raises
        ------
        EOFError
            Reached end of file

        """
        data = self.iqfile.read(self.buffer_size)
        if not data:
            raise EOFError()
        data = np.frombuffer(data, dtype=np.complex64)
        return Samples(data=data, sample_rate=self.sample_rate)

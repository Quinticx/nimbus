import numpy as np
from nimbus import Samples
import pathlib
import json


class IQ:
    """IQ is a source that reads from an .iq file and returns a numpy array"""

    def __init__(self, filename: pathlib.Path, buffer_size: int = 2048):
        self.filename = filename
        self.iqfile = open(self.filename, "rb")
        self.buffer_size = buffer_size
        jsonfile = open(filename.with_suffix(".json"), "r")
        info = json.load(jsonfile)
        self.sample_rate = info["sample_rate"]

    def read(self):
        """Read .iq file and return signal"""
        data = self.iqfile.read(self.buffer_size)
        if not data:
            raise EOFError()
        data = np.frombuffer(data, dtype=np.complex64)
        return Samples(data=data, sample_rate=self.sample_rate)

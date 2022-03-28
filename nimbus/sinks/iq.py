import numpy as np
from nimbus import Samples
import json


class IQ:
    """IQ is a sink that saves a signal to a .iq file"""

    def __init__(self, filename: str = "output.iq"):
        self.filename = filename
        self.iqfile = open(self.filename, "wb")
        self.has_run = False
        self.jsonfilename = self.filename.with_suffix(".json")
        self.jsonfile = open(self.jsonfilename, "w")

    def execute(self, signal: Samples):
        """Writes signal to a .iq file"""
        if not signal.data.dtype == np.complex64:
            raise ValueError(f"IQ Sink requires np.complex64 signal: {signal.data.dtype}")

        if not self.has_run:

            json.dump({"sample_rate": signal.sample_rate}, self.jsonfile)
            self.has_run = True
        signal = signal.data.astype(np.complex64)
        signal = signal.tobytes()
        self.iqfile.write(signal)

    def close(self):
        self.iqfile.close()
        self.jsonfile.close()

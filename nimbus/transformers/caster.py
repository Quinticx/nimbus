import numpy as np
from nimbus import Samples

transforms = {
    np.complex128: {
        np.complex128: lambda x: x,
        np.complex64: lambda x: x.astype(np.complex64),
    },
    np.complex64: {
        np.complex64: lambda x: x,
        np.complex128: lambda x: x.astype(np.complex128),
    },
    np.float64: {
        np.float64: lambda x: x,
        np.float32: lambda x: x.astype(np.float32),
        np.int16: lambda x: (x * np.iinfo(np.int16).max).astype(np.int16),
        np.uint8: lambda x: ((x + 1) * (np.iinfo(np.uint8).max / 2)).astype(np.uint8),
    },
    np.float32: {
        np.float32: lambda x: x,
        np.float64: lambda x: x.astype(np.float64),
        np.int16: lambda x: (x * np.iinfo(np.int16).max).astype(np.int16),
        np.uint8: lambda x: ((x + 1) * (np.iinfo(np.uint8).max / 2)).astype(np.uint8),
    },
    np.int16: {
        np.float32: lambda x: (x.astype(np.float32)) / (np.iinfo(np.int16).max),
        np.float64: lambda x: (x.astype(np.float64)) / (np.iinfo(np.int16).max),
        np.int16: lambda x: x,
        np.uint8: lambda x: (
            (x + np.iinfo(np.int16).max)
            / ((2 * np.iinfo(np.int16).max) / (np.iinfo(np.uint8).max))
        ).astype(np.uint8),
    },
}


class Caster:
    """
    Caster is a transformer that takes in a signal of one type and casts it to another type

    Attributes
    ----------
    transforms
        Dictionary of numpy type conversions

    Notes
    -----
        Caster is used when converting between Sources, Transformers, or Sinks.
    """

    def __init__(self, dtype: np.dtype):
        """
        Constructs new Caster

        Parameters
        ----------
        dtype: np.dtype
            Type signal should be converted to.

        """
        self.dtype = dtype

    def execute(self, signal: Samples) -> Samples:
        """
        Converts signal to new type

        Parameters
        ----------
        signal: Samples
            Signal to be converted

        Returns
        -------
        signal: Samples
            Returns signal.data of new signal type

        Raises
        ------
        ValueError
            Cannot convert signal type to new type.

        """
        signal_type = signal.data.dtype.type
        try:
            return signal.replace(data=transforms[signal_type][self.dtype](signal.data))
        except KeyError:
            raise ValueError(f"Cannot convert {signal_type} to {self.dtype}")

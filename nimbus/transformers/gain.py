from nimbus import Samples


class Gain:
    """
    Gain is a transformer that applies a gain to a signal

    Attributes
    ----------
    gain: float
        Amount to gain signal by

    """

    def __init__(self, gain: float):
        """
        Constructs a new Gain transformer with a gain of gain

        Parameters
        ----------
        gain: float
            The gain of the transformer
        """
        self.gain = gain

    def execute(self, signal: Samples) -> Samples:
        """
        Applies a gain to the input

        Parameters
        ----------
        signal: Samples
            The signal to gain

        Returns
        -------
        signal: Samples
            Returns signal.data with gained signal
        """
        return signal.replace(data=signal.data * self.gain)

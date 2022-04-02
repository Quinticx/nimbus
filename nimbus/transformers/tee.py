from nimbus import Samples


class Tee:
    """
    Tee is a transformer class that passes along it's input while also sending a copy to an extra sink

    Attributes
    ----------
    sink: Sink
        Extra sink to send signal to.

    """

    def __init__(self, sink):
        """
        Constructs new Tee transformer

        Parameters
        ----------
        sink: Sink
            Extra sink to send signal to
        """
        self.sink = sink

    def execute(self, signal: Samples) -> Samples:
        """
        Sends signal to extra sink

        Parameters
        ----------
        signal: Samples
            Input signal to pass along to sinks

        Returns
        -------
        signal: Samples
            Passes signal to original Sink destination
        """
        self.sink.execute(signal)
        return signal

    def close(self):
        """
        Closes Sink
        """
        self.sink.close()

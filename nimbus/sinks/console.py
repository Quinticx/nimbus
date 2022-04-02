from nimbus import Samples


class Console:
    """
    Console is a sink class that prints a signal to the console

    Notes
    -----
        This class is for testing purposes.

    """

    def __init__(self):
        """
        Constructs new Console Sink
        """
        pass

    def execute(self, signal: Samples):
        """
        Prints signal to console

        Parameters
        ----------
        signal: Samples
            Input signal to print.

        """
        print(signal.data)
        return

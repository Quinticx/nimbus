from nimbus import Samples


class Tee:
    """Tee is a transformer that passes along it's input while also sending a copy to an extra sink"""

    def __init__(self, sink):
        self.sink = sink

    def execute(self, signal: Samples) -> Samples:
        self.sink.execute(signal)
        return signal

    def close(self):
        self.sink.close()

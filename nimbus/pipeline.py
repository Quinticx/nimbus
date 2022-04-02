class Pipeline:
    """

    Attributes
    ----------
    source: Source
        Input Source
    transformers: Transformers
        List of transforms to be performed
    sink: Sink
        Output Sink

    """

    def __init__(self, source, transformers, sink):
        """
        Constructs a new Pipeline

        Parameters
        ----------
        source: Source
            Input Source
        transformers: Transformers
            List of transforms to be performed
        sink: Sink
            Output Sink

        """
        self.source = source
        self.transformers = transformers
        self.sink = sink

    def run(self, num_iter: int = None):
        """
        Starts the Pipeline and runs until no transforms are left

        Parameters
        ----------
        num_iter: int
            Number of iterations


        """
        index = 0
        while num_iter is None or index < num_iter:
            index += 1
            try:
                sample = self.source.read()

                for t in self.transformers:
                    sample = t.execute(sample)

                self.sink.execute(sample)
            except (EOFError, KeyboardInterrupt) as e:
                for t in self.transformers:
                    try:
                        t.close()
                    except AttributeError:
                        pass
                try:
                    self.sink.close()
                except AttributeError:
                    pass
                return

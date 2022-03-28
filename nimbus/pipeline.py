class Pipeline:
    def __init__(self, source, transformers, sink):
        self.source = source
        self.transformers = transformers
        self.sink = sink

    def run(self, num_iter: int = None):
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

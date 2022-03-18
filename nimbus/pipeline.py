class Pipeline:
    def __init__(self, source, transformers, sink):
        self.source = source
        self.transformers = transformers
        self.sink = sink

    def run(self, num_iter: int = 200):
        for i in range(num_iter):
            try:
                sample = self.source.read()

                for t in self.transformers:
                    sample = t.execute(sample)

                self.sink.execute(sample)
            except IndexError:
                return

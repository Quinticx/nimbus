import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
import numpy as np
from pathlib import Path

sdr_source = nimbus.sources.SDR(sample_rate=2.56e5, frequency=9.91e7)
iq_sink = nimbus.sinks.IQ(Path("examples/test_iq.iq"))
console_sink = nimbus.sinks.Console()

pipeline = nimbus.Pipeline(
    sdr_source,
    [],
    iq_sink,
)
pipeline.run()

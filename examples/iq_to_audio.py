import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
from pathlib import Path

iq_source = nimbus.sources.IQ(Path("examples/test_tee_iq.iq"))
audio_sink = nimbus.sinks.Audio()
console_sink = nimbus.sinks.Console()

pipeline = nimbus.Pipeline(
    iq_source,
    [
        nimbus.transformers.FM_Demod(),
        nimbus.transformers.Resample(44700),
        nimbus.transformers.Gain(2),
    ],
    audio_sink,
)
pipeline.run()

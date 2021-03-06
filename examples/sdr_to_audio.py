import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
import numpy as np

sdr_source = nimbus.sources.SDR(sample_rate=2.56e5, frequency=10.77e7)
audio_sink = nimbus.sinks.Audio()
console_sink = nimbus.sinks.Console()

pipeline = nimbus.Pipeline(
    sdr_source,
    [
        nimbus.transformers.Caster(np.complex64),
        nimbus.transformers.FM_Demod(),
        nimbus.transformers.Resample(44700),
        nimbus.transformers.Gain(2),
        nimbus.transformers.Caster(np.float32),
    ],
    audio_sink,
)
pipeline.run()

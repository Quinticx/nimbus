import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
from pathlib import Path
import numpy as np

sdr_source = nimbus.sources.SDR(sample_rate=2.56e5, frequency=9.91e7)
audio_sink = nimbus.sinks.Audio()
iq_sink = nimbus.sinks.IQ(Path("examples/test_tee_iq.iq"))
wave_sink = nimbus.sinks.Wave("examples/test_tee_wave.wav")

pipeline = nimbus.Pipeline(
    sdr_source,
    [
        nimbus.transformers.Caster(np.complex64),
        nimbus.transformers.Tee(iq_sink),
        nimbus.transformers.FM_Demod(),
        nimbus.transformers.Caster(np.int16),
        nimbus.transformers.Tee(wave_sink),
        nimbus.transformers.Resample(44700),
        nimbus.transformers.Gain(2),
        nimbus.transformers.Caster(np.float32),
    ],
    audio_sink,
)
pipeline.run()

import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
from pathlib import Path
import numpy as np

sync_frame = np.array(
    [
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        1,
        1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ]
)

sdr_source = nimbus.sources.SDR(sample_rate=2.56e5, frequency=137.62e6)
image_sink = nimbus.sinks.Image("examples/noaa.png")
iq_sink = nimbus.sinks.IQ(Path("examples/noaa.iq"))
wave_sink = nimbus.sinks.Wave("examples/noaa.wav")

pipeline = nimbus.Pipeline(
    sdr_source,
    [
        nimbus.transformers.Caster(np.complex64),
        nimbus.transformers.Tee(iq_sink),
        nimbus.transformers.FM_Demod(),
        nimbus.transformers.Caster(np.int16),
        nimbus.transformers.Tee(wave_sink),
        nimbus.transformers.Resample(sample_rate=4160),
        nimbus.transformers.Caster(np.float32),
        nimbus.transformers.Apt_Sync(sync_frame),
        nimbus.transformers.Caster(np.uint8),
    ],
    image_sink,
)
pipeline.run()

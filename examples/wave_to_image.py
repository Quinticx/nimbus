import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
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
wave_source = nimbus.sources.Wave("examples/10080101_16bit.wav", buffer_size=5512)
image_sink = nimbus.sinks.Image("examples/test_image_16bit_resampled.png")
console_sink = nimbus.sinks.Console()

pipeline = nimbus.Pipeline(
    wave_source,
    [
        nimbus.transformers.Caster(np.float32),
        nimbus.transformers.Hilbert(),
        nimbus.transformers.Tee(console_sink),
        nimbus.transformers.Resample(sample_rate=4160),
        nimbus.transformers.Apt_Sync(sync_frame),
        nimbus.transformers.Caster(np.uint8),
    ],
    image_sink,
)
pipeline.run()

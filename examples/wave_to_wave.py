import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
import numpy as np

wave_source = nimbus.sources.Wave("examples/10080101_16bit.wav", buffer_size=5512)
#wave_source = nimbus.sources.Wave("examples/owl_beep.wav", buffer_size=100)
wave_sink = nimbus.sinks.Wave("examples/test_wave.wav")
console_sink = nimbus.sinks.Console()

pipeline = nimbus.Pipeline(
    wave_source,
    [
        nimbus.transformers.LowPass(),
        #nimbus.transformers.Caster(np.int16)
    ],
    wave_sink,
)
pipeline.run()

import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers

wave_source = nimbus.sources.Wave("examples/10080101_16bit.wav", buffer_size=5512)
audio_sink = nimbus.sinks.Audio()

pipeline = nimbus.Pipeline(
    wave_source,
    [],
    audio_sink,
)
pipeline.run()

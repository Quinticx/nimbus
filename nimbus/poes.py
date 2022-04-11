from nimbus import Pipeline
import nimbus
import nimbus.sources
import nimbus.sinks
import nimbus.transformers
import numpy as np
import pathlib
import typing

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
sample_rate = int(2.56e5)
wave_rate = 5512
baud_rate = 4160


def pipeline(
    sdr_enabled: bool,
    iq_source: typing.Optional[pathlib.Path],
    wave_source: typing.Optional[pathlib.Path],
    iq_sink: typing.Optional[pathlib.Path],
    wave_sink: typing.Optional[pathlib.Path],
    image_sink: typing.Optional[pathlib.Path],
    audio_enabled: bool,
    frequency: float,
) -> Pipeline:

    source = None
    if sdr_enabled:
        source = nimbus.sources.SDR(sample_rate=sample_rate, frequency=frequency)
    elif iq_source is not None:
        source = nimbus.sources.IQ(iq_source, buffer_size=sample_rate)
    elif wave_source is not None:
        source = nimbus.sources.Wave(wave_source, buffer_size=wave_rate)
    else:
        raise ValueError("Must set one of: iq_source, wave_source, or sdr_enabled")

    transformer_list = []

    if sdr_enabled:
        transformer_list.append(nimbus.transformers.Caster(np.complex64))
        if iq_sink:
            transformer_list.append(nimbus.transformers.Tee(nimbus.sinks.IQ(iq_sink)))
    if iq_source or sdr_enabled:
        transformer_list.append(nimbus.transformers.FM_Demod())
        transformer_list.append(nimbus.transformers.Caster(np.int16))
        if wave_sink:
            transformer_list.append(
                nimbus.transformers.Tee(nimbus.sinks.Wave(wave_sink))
            )

    transformer_list.append(nimbus.transformers.Caster(np.float32))

    if audio_enabled:
        transformer_list.append(nimbus.transformers.Tee(nimbus.sinks.Audio()))

    transformer_list.append(nimbus.transformers.Hilbert())
    transformer_list.append(nimbus.transformers.Resample(sample_rate=baud_rate))
    transformer_list.append(nimbus.transformers.Caster(np.float32))
    transformer_list.append(nimbus.transformers.Apt_Sync(sync_frame))
    transformer_list.append(nimbus.transformers.Caster(np.uint8))

    if image_sink:
        transformer_list.append(nimbus.transformers.Tee(nimbus.sinks.Image(image_sink)))

    return nimbus.Pipeline(
        source,
        transformer_list,
        nimbus.sinks.SDL(width=2080, height=1000),
    )


def id_to_freq(satellite: str) -> float:
    frequency_dict = {
        "15": 99.1e6,
        "18": 137.9125e5,
        "19": 137.1e5,
    }
    return frequency_dict[satellite]

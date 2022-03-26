import numpy as np
import scipy.io.wavfile as spwave
from numpy.testing import assert_array_equal
import pytest as pt
from nimbus.sources import Wave as ws
from nimbus.sinks import Wave as wf
from nimbus.transformers import Gain
from nimbus import Pipeline, Samples
from test.mocks import MockSink, MockSource


def test_wavefile(tmp_path):
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2.0 * np.pi * fs * t)
    expected_data = data.astype(np.int16)
    filename = tmp_path / "test_wave.wav"

    test_source = MockSource(expected_data, sample_rate=samplerate)
    wave_sink = wf(filename)

    pipeline1 = Pipeline(test_source, [Gain(1)], wave_sink)
    pipeline1.run()

    wave_source = ws(filename)
    test_sink = MockSink()

    pipeline2 = Pipeline(wave_source, [Gain(1)], test_sink)
    pipeline2.run()

    actual_data = test_sink.get_buffer()

    assert_array_equal(expected_data, actual_data)


def test_wavesink(tmp_path):
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    expected_data = amplitude * np.sin(2.0 * np.pi * fs * t)
    expected_data = expected_data.astype(np.int16)
    filename = tmp_path / "test_wave.wav"

    test_source = MockSource(expected_data, sample_rate=samplerate)
    test_sink = wf(filename)

    pipeline = Pipeline(test_source, [Gain(1)], test_sink)
    pipeline.run()

    frame_rate, actual_data = spwave.read(filename)
    assert_array_equal(expected_data, actual_data)
    assert samplerate == frame_rate


def test_wavesource(tmp_path):
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2.0 * np.pi * fs * t)
    filename = tmp_path / "test_wav.wav"
    spwave.write(filename, samplerate, data.astype(np.int16))

    test_sink = MockSink()
    source = ws(filename)
    pipeline = Pipeline(source, [Gain(1)], test_sink)
    pipeline.run()
    test_signal = test_sink.get_buffer()

    assert_array_equal(data.astype(np.int16), test_signal)

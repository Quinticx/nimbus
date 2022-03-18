import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from nimbus.sources import Wave as ws
from nimbus.sinks import Wave as wf


def test_wavefile():
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2.0 * np.pi * fs * t)
    data = data.astype(np.int16)
    test_sink = wf()
    test_sink.write(data)
    test_source = ws("output.wav")
    test_signal, frame_rate = test_source.read()
    assert_array_equal(data, test_signal)


def test_wavesink():
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2.0 * np.pi * fs * t)

    test_sink = wf(frame_rate=samplerate)
    test_sink.write(data)


def test_wavesource():
    samplerate = 44100
    fs = 100
    t = np.linspace(0.0, 1.0, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2.0 * np.pi * fs * t)

    test_source = ws("output.wav")
    test_signal, frame_rate = test_source.read()

    assert_array_equal(data.astype(np.int16), test_signal)

import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from test.mocks import MockSource
from test.mocks import MockSink


def test_mock_source():
    r = np.random.rand(15)
    signal = MockSource(r, 5)
    signal1 = signal.generate()
    assert_array_equal(signal1, r[0:5])

    signal2 = signal.generate()
    assert_array_equal(signal2, r[5:10])

    signal3 = signal.generate()
    assert_array_equal(signal3, r[10:15])

    with pt.raises(IndexError):
        signal4 = signal.generate()


def test_mock_sink():
    signal = np.random.rand(15)
    sink = MockSink()
    sink.console_print(signal[0:5])
    sink.console_print(signal[5:10])
    sink.console_print(signal[10:15])
    test_signal = sink.get_buffer()
    assert_array_equal(signal, test_signal)

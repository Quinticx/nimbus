import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from test.mocks import MockSource
from test.mocks import MockSink
from nimbus import Samples


def test_mock_source():
    r = np.random.rand(15)
    signal = MockSource(r, 5)
    signal1 = signal.read().data
    assert_array_equal(signal1, r[0:5])

    signal2 = signal.read().data
    assert_array_equal(signal2, r[5:10])

    signal3 = signal.read().data
    assert_array_equal(signal3, r[10:15])

    with pt.raises(EOFError):
        signal.read().data


def test_mock_sink():
    signal = np.random.rand(15)
    sink = MockSink()
    sink.execute(Samples(signal[0:5]))
    sink.execute(Samples(signal[5:10]))
    sink.execute(Samples(signal[10:15]))
    test_signal = sink.get_buffer()
    assert_array_equal(signal, test_signal)

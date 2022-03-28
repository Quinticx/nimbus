from nimbus import Pipeline
from nimbus.transformers import Gain
import numpy as np
from numpy.testing import assert_array_equal
from test.mocks import MockSource
from test.mocks import MockSink


def test_pipeline():

    signal = np.random.rand(15)
    test_sink = MockSink()
    pipe = Pipeline(MockSource(signal), [Gain(3)], test_sink)
    pipe.run()
    test_signal = test_sink.get_buffer()
    assert_array_equal(signal * 3, test_signal)

from test.mocks import MockSink, MockSource
from nimbus.transformers import Gain, Tee
from nimbus import Pipeline
import numpy as np
from numpy.testing import assert_array_equal

def test_tee():
    expected_data = np.random.rand(10)

    test_sink = MockSink()
    test_source = MockSource(expected_data)
    test_tee_sink = MockSink()

    pipeline = Pipeline(test_source, [Tee(test_tee_sink), Gain(2)], test_sink)
    pipeline.run()

    tee_output = test_tee_sink.get_buffer()
    test_output = test_sink.get_buffer()

    assert_array_equal(expected_data, tee_output)

    assert_array_equal(expected_data*2, test_output)

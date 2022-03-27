from nimbus.sinks import IQ as iqf
from nimbus.sources import IQ as iqs
from nimbus import Pipeline, Samples
from test.mocks import MockSink, MockSource
import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt


def test_iqfile(tmp_path):
    filename = tmp_path / "test_iq.iq"
    expected_data = np.random.random(10) + np.random.random(10) * 1j
    expected_data = expected_data.astype(np.complex64)
    test_source = MockSource(expected_data)
    iq_sink = iqf(filename)

    pipeline1 = Pipeline(test_source, [], iq_sink)
    pipeline1.run()

    iq_source = iqs(filename)
    test_sink = MockSink()

    pipeline2 = Pipeline(iq_source, [], test_sink)
    pipeline2.run()

    actual_data = test_sink.get_buffer()

    assert_array_equal(expected_data, actual_data)

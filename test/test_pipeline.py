from nimbus.sources import Random
from nimbus import Pipeline
from nimbus.transformers import Gain
import numpy.typing as npt
import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from test.mocks import MockSource
from test.mocks import MockSink
from nimbus.sources import Wave
from nimbus.sinks import Image as imf


def test_pipeline():

    signal = np.random.rand(15)
    test_sink = MockSink()
    pipe = Pipeline(MockSource(signal), [Gain(3)], test_sink)
    pipe.run()
    test_signal = test_sink.get_buffer()
    assert_array_equal(signal * 3, test_signal)

def test_pipeline_image():
    test_source = Wave("10080101.wav")
    test_sink = imf()
    pipe = Pipeline(test_source,[Gain(1)], test_sink )
    pipe.run()



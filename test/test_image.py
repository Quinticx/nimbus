import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from nimbus.sources import Image as ims
from nimbus.sinks import Image as imf
from nimbus import Pipeline
from PIL import Image as pil
from test.mocks import MockSink, MockSource

def test_image_source(tmp_path):
    data = np.random.rand(25)
    expected_data = np.uint8(data*255)
    data = np.resize(expected_data, (5,5))
    expected_image = pil.fromarray(data, "L")
    filename = tmp_path / "test_image.png" 
    expected_image.save(filename)
    
    img_source = ims(filename)
    test_sink = MockSink()

    pipeline = Pipeline(img_source, [], test_sink)
    pipeline.run()

    actual_data = test_sink.get_buffer()
    assert_array_equal(expected_data, actual_data)
    
def test_image_sink(tmp_path):
    data = np.random.rand(25)
    expected_data = np.uint8(data*255)
    filename = tmp_path / "test_image.png" 

    test_source = MockSource(expected_data)
    img_sink = imf(filename)

    pipeline = Pipeline(test_source, [], img_sink)
    pipeline.run()
    
    img = pil.open(filename) 
    actual_data = np.array(img).flatten()
    assert_array_equal(expected_data, actual_data)

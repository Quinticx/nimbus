import numpy as np
from numpy.testing import assert_array_equal
from nimbus.sources import Image as ims
from nimbus import Pipeline
from PIL import Image as pil
from test.mocks import MockSink


def test_image_source(tmp_path):
    data = np.random.rand(25)
    expected_data = np.uint8(data * 255)
    data = np.resize(expected_data, (5, 5))
    expected_image = pil.fromarray(data, "L")
    filename = tmp_path / "test_image.png"
    expected_image.save(filename)

    img_source = ims(filename)
    test_sink = MockSink()

    pipeline = Pipeline(img_source, [], test_sink)
    pipeline.run()

    actual_data = test_sink.get_buffer()
    assert_array_equal(expected_data, actual_data)

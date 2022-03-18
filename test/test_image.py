import numpy as np
from numpy.testing import assert_array_equal
import pytest as pt
from nimbus.sources import Image as ims
from nimbus.sinks import Image as imf


def test_imagefile():
    i_source = ims()
    imarray = i_source.read("bri.jpg")

    i_sink = imf()
    i_sink.execute(imarray)

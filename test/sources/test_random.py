from nimbus.sources import Random
import numpy as np
from numpy.testing import assert_array_equal


def test_random():
    r = Random(3)
    signal = r.generate()

    assert np.size(signal) == 3

    assert np.all((signal < 1) & (signal >= 0))

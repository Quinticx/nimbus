from nimbus.sources import Random
import numpy as np


def test_random():
    r = Random(3)
    signal = r.generate().data

    assert np.size(signal) == 3

    assert np.all((signal < 1) & (signal >= 0))

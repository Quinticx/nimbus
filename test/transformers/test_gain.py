from nimbus.transformers import Gain
import numpy as np
from numpy.testing import assert_array_equal
from nimbus import Samples


def test_gain_identity():
    g = Gain(1)
    signal = np.random.uniform(size=10)
    tg = g.execute(Samples(signal)).data

    assert_array_equal(tg, signal)


def test_gain_up():
    g = Gain(10)
    signal = np.random.uniform(size=10)
    tg = g.execute(Samples(signal)).data

    assert_array_equal(tg, 10 * signal)


def test_gain_down():
    g = Gain(-10)
    signal = np.random.uniform(size=10)
    tg = g.execute(Samples(signal)).data

    assert_array_equal(tg, -10 * signal)

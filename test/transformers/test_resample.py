from nimbus import Samples
from nimbus.transformers import Resample
import numpy as np
from numpy.testing import assert_array_equal


def test_resample():
    test_signal = np.ones(10)
    resampled = Resample(sample_rate=2)

    actual_samples = resampled.execute(Samples(test_signal, 1))

    expected_signal = np.ones(20)

    assert_array_equal(expected_signal, actual_samples.data)

    assert actual_samples.sample_rate == 2

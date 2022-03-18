from nimbus.transformers import Hilbert
import numpy as np
from numpy.testing import assert_array_equal
from scipy.signal import chirp, hilbert


def test_hilbert_chirp():
    duration = 1
    fs = 400.0
    samples = int(fs * duration)
    t = np.arange(samples) / fs

    signal = chirp(t, 20.0, t[-1], 100.0)
    signal *= 1.0 + 0.5 * np.sin(2.0 * np.pi * 3.0 * t)

    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)

    hb = Hilbert()
    test_envelope = hb.execute(signal)

    assert_array_equal(test_envelope, amplitude_envelope)

import numpy as np
import pytest as pt
from numpy.testing import assert_array_equal
from nimbus.transformers import Apt_Sync
from nimbus import Samples
from nimbus.transformers.aptsync import find_sync_frame


def test_apt_sync_same():
    sync_frame = np.array([1, 0] * 10)
    test_signal = np.random.rand(len(sync_frame) * 5)
    test_signal = np.insert(test_signal, len(sync_frame) * 2, sync_frame)
    expected = test_signal[: len(sync_frame) * 2]

    apt = Apt_Sync(sync_frame)
    actual = apt.execute(Samples(test_signal)).data
    assert_array_equal(expected, actual)


def test_find_sync():
    sync_frame = np.array([1, 0] * 10)
    test_signal = np.random.rand(len(sync_frame) * 5)
    new_signal = np.insert(test_signal, len(sync_frame) * 2, sync_frame)

    index = find_sync_frame(new_signal, sync_frame)
    assert index == len(sync_frame) * 2 - 1


def test_find_sync_fail():
    sync_frame = np.array([1, 0] * 10)
    test_signal = np.random.rand(180)

    with pt.raises(EOFError):
        find_sync_frame(test_signal, sync_frame)

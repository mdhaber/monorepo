import package1
import numpy as np


def test_sin():
    x = 1.0
    np.testing.assert_equal(package1.sin(x), np.sin(x))


def test_cos():
    x = 1.0
    np.testing.assert_equal(package1.cos(x), np.cos(x))

import package2
import numpy as np


def test_tan():
    x = 1.0
    np.testing.assert_equal(package2.tan(x), np.tan(x))

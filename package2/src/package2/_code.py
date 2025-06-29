# _code.py
import package1
import numpy as np

__all__ = ["cos"]  # Only 'sin' is accessible when using `from package1 import *`


def cos(x):
    """
    Summary of the function.

    Parameters
    ----------
    x : float
        Description of the first parameter.

    Returns
    -------
    float
        The ``cos`` of x.
    """
    return package1.sin(x + np.pi / 2)

# _code.py
import numpy as np

__all__ = ["sin"]  # Only 'sin' is accessible when using `from package1 import *`


def sin(x):
    """
    Summary of the function.

    Parameters
    ----------
    x : float
        Description of the first parameter.

    Returns
    -------
    float
        The ``sin`` of x.

    Examples
    --------
    >>> import package1
    >>> package1.sin(0)
    np.float64(0.0)
    """
    return np.sin(x)


def _cos(x):
    return np.cos(x)

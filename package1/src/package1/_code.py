# _code.py
import numpy as np

__all__ = ["sin", "cos"]


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

    Examples
    --------
    >>> import package1
    >>> package1.cos(0)
    np.float64(1.0)
    """
    return np.cos(x)

# The function will evaluate the pth order polynomial interpolate of a function f
# at set of points xhat. Where the nodal interpolation points are uniformly space
# over the interval [a, b]. The output interp is a vector containing the values
# evaluated at corresponding xhat.
# Input: [a, b] - given interval
#        p - order of the polynomial
#        xhat - set of nodal points
#        f - given function

import math
import numpy as np
from lagrangePoly import lagrangePoly


def func(x):
    y = np.cos(np.pi * x) + x
    return y


def polyInterpolation(a, b, p, xhat):
    y = np.array([])
    x = np.linspace(a, b, p + 1)
    n = len(xhat)
    [L, errorFlag] = lagrangePoly(p, x, n, xhat)
    for i in range(p + 1):
        y = np.append(y, func(x[i]))
    interp = np.dot(y, L)
    return interp


# Example
a = -0.5
b = 0.5
p = 3
xhat = np.linspace(-1, 1, 6)
print(polyInterpolation(a, b, p, xhat))

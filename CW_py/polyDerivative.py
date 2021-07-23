# The function will finds the derivative of the pth order polynomial
# interpolant of a function at a point x
# Input: x - evaluation point
#        p - integer polynomial degree
#        h - width of the interval be separated
#        k - additional input to make x_k = x
#        f - given function to be evaluated
# Output: dInterp - a single value containing the approximation to the derivative at x


import numpy as np
from derivLagrangePoly import derivLagrangePoly


def func(x):
    y = np.cos(np.pi * x) + x
    return y


def polyDerivative(x, p, h, k):
    xhat = x
    x = np.arange(x - k * h, x + (p - k) * h, h)
    n = len([k])
    y = np.array([])
    LDiff = derivLagrangePoly(p, x, n, xhat)
    for i in range(len(x)):
        y = np.append(y, func(x[i]))

    dInterp = np.dot(LDiff.T, y)
    return dInterp


# Example
# p = 3
# h = 0.1
# x = 0.5
# k = 0
# print(polyDerivative(x, p, h, k))

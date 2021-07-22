# fpiter_func will compute the vector of approximtions p_vec
# obtained by fixed-point iteration applied to function g(x) = x - c* f(x),
# using Nmax iterations, and initial guess p0

import math
import numpy as np


def func(x):
    y = x ** 2 - 3 * x
    return y


def gfunc(x, c):
    g = x - c * func(x)
    return g


def fpiter_func(c, p0, Nmax):
    p_vec = []
    p = p0
    for i in range(Nmax):
        p = gfunc(p, c)
        p_vec.append(p)
    return p_vec

# Example
# print(fpiter_func(1, 0.5, 10))

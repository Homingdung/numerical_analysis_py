# bisection_func will computes the vector of approximations p_vec obtained by
# the bisection method applied to function f, using Nmax iterations, and interval [a, b]

import math
import numpy as np


def bisection_func(a, b, Nmax):
    p_vec = []
    for i in range(Nmax):
        p = (a + b) / 2
        if func(p) * func(a) > 0:
            a = p
        else:
            b = p
        p_vec.append(p)
    return p_vec


# function
def func(x):
    y = x ** 2 - 3 * x - 2
    return y


# Example
print(bisection_func(-5, 5, 5))


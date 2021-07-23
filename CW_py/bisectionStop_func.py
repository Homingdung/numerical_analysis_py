# BisectionStop_func will computes the vector of approximations p_vec
# obtained by the bisection method applied to function f, using a maximum
# of Nmax iterations, and TOL as a tolerance, and interval [a,b]
import math
import numpy as np


def bisectionStop_func(a, b, Nmax, TOL):
    p_vec = []
    for i in range(Nmax):
        p = (a + b) / 2
        if func(p) * func(a) > 0:
            a = p
        else:
            b = p
        p_vec.append(p)
        if i > 1 and abs(p_vec[i] - p_vec[i - 1]) < TOL:
            break
    return p_vec


def func(x):
    y = x ** 2 - 3 * x - 2
    return y

# Example
# print(bisectionStop_func(-5, 5, 100, 0.00001))

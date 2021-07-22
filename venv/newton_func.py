# newton_func will compute the vector oc approximations p_vec
# obtained by Newton's method applied to function f with derivative dfdx,
# using Nmax iterations, and initial guess p0

import math
import numpy as np
from sympy import *


# function
def func(x):
    y = x ** 3 - 3
    return y


# derivative of the function
def df(x):
    dy = 3 ** x * 2
    return dy


# Newton' s method
def newton_func(p0, Nmax):
    p_vec = []
    for i in range(Nmax):
        p = p0 - func(p0) / df(p0)
        p_vec.append(p)
    return p_vec



# Example
# print(newton_func(0.5, 10))

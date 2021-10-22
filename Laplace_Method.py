# This is a verification of laplace method for asymptotic analysis
import scipy.integrate as integrate
import numpy as np


# define a function f(t)
def func(t):
    f = -7 * t ** 2 + 5 * t ** 3 - t ** 4
    return f


# set value for I(x)

x = 10
result = integrate.quad(lambda t: np.exp(x * func(t)), 7 / 4, np.inf)
print(result)

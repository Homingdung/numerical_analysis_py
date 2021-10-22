# This is a verification of laplace method for asymptotic analysis
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt


# define a function f(t)
def func(t):
    f = -7 * t ** 2 + 5 * t ** 3 - t ** 4
    return f


# set value for I(x), as x becomes larger and larger...

x = [10, 100]
y = []
for i in range(len(x)):
    result = integrate.quad(lambda t: np.exp(x[i] * func(t)), 7 / 4, np.inf)
    y.append(result[0])

print(y)

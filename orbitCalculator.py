# Calculation for the orbit length, average speed and the perigee speed of the satellite
# Fact: h1 = 200 km, h2 = 51000 km, R = 6378 km, T = 16 hour
# result: The orbit length - 163911 km
#         Average speed - 2.846 km /s
#         perigee speed - 10.302 km/s

import math

import numpy as np
from scipy import integrate


h1 = 200
h2 = 51000
R = 6378
a = (h1 + h2) / 2 + R
c = (h2 - h1) / 2
b = np.sqrt(a ** 2 - c ** 2)
T = 16 * 3600


def func(x):
    y = np.sqrt(a ** 2 * np.cos(x) ** 2 + b ** 2 * np.sin(x) ** 2)
    return y


L = 4 * integrate.quad(func, 0, np.pi / 2)[0]
L = np.array(L, dtype=float)
v = L / T
vmax = 2 *np.pi * a * b / T / (h1 + R)


print(L)
print(v)
print(vmax)
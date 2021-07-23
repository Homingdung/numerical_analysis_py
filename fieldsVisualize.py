# This demo shows how to plot the contour plot for given function, with resultant of the partial derivatives displayed
# as arrows

import numpy as np
import matplotlib.pyplot as plt
import math


def func(x, y):
    z = y - x - 2 * x ** 2 - 2 * x * y - y ** 2
    return z


x = np.linspace(-2, 0, 20)
y = np.linspace(1, 3, 20)
[X, Y] = np.meshgrid(x, y)
Z = func(X, Y)
[fx, fy] = np.gradient(Z, 0.25)
vs1 = plt.contour(x, y, Z)
vs2 = plt.quiver(x, y, -fx, -fy)
plt.title("Contour plot & partial derivatives")
plt.show()
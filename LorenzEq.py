# This is a visualization of Lorenz equation
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

xs, ys, zs = [], [], []
s, r, b = 10.0, 28.0, 8.0 / 3.0
dt = 0.01
x0, y0, z0 = 0.1, 0, 0
for i in range(10000):
    x1 = x0 + dt * s * (y0 - x0)
    y1 = y0 + dt * (x0 * (r - z0) - y0)
    z1 = z0 + dt * (x0 * y0 - b * z0)
    x0, y0, z0 = x1, y1, z1
    xs.append(x0)
    ys.append(y0)
    zs.append(z0)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(xs, ys, zs, color='r')
plt.title("Lorenz attractor")
plt.show()

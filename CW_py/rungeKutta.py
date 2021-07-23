# The function will solve the ODE by Runge-Kutta methods
# Input: [a, b] - interval
#        f - RHS of the differential equation systems
#        N - number of subintervals for [a, b]
#        y0 - initial value for IVP
#        m - length of the ODE system
#        method = 1 Forward Euler Method
#        method = 2 Modified Euler Method
#        method = 4 The RK4 Method
# Output: t - vector containing the nodal points
#         y - matrix containing the approximations corresponding to all time points
import numpy as np


def func(t, y):
    f = y - t ** 2 + 1
    return f


def rungeKutta(a, b, N, y0, method):
    y = np.array([])
    y = np.append(y, y0)
    h = (b - a) / N
    t = np.arange(a, b, h)
    if method == 1:
        for i in range(N):
            y = np.append(y, y[i] + h * func(t[i], y[i]))
    elif method == 2:
        for i in range(N - 1):
            Y = y[i] + h * func(t[i], y[i])
            y = np.append(y, y[i] + (h / 2) * (func(t[i], y[i]) + func(t[i + 1], Y)))

    else:
        for i in range(N):
            K1 = func(t[i], y[i])
            K2 = func(t[i] + h / 2, y[i] + h / 2 * K1)
            K3 = func(t[i] + h / 2, y[i] + h / 2 * K2)
            K4 = func(t[i] + h, y[i] + h * K3)
            y = np.append(y, y[i] + (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4))
    return y


# Example
a = 0
b = 1
N = 10
y0 = np.array([0])
method = 2
print(rungeKutta(a, b, N, y0, method))

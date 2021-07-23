# The function will find the p + 1 lagrange interpolating polynomials
# given a set of nodal points
# Input: p - integer polynomial degree
#        x - set of p+1 nodal point
#        n - number of points in evaluation vector
#        xhat - set of evaluation points
# Output:L - matrix containing the evaluated lagrange polynomials
#        errorFlag - return 1 if nodal points are indistinct


import numpy as np


def lagrangePoly(p, x, n, xhat):
    tol = 0.000000000012
    L = np.ones((p + 1, n))
    errorFlag = 0
    for k in range(0, p + 1):
        for m in range(0, p + 1):
            if m != k:
                if abs(x[k] - x[m] < tol):
                    errorFlag = 1
                L[k, :] = L[k, :] * (xhat - x[m]) / (x[k] - x[m])

    return L, errorFlag



# Example
# x = np.linspace(-0.5, 0.5, 4)
# p = 3
# n = 6
# xhat = np.linspace(-1, 1, 6)
# print(lagrangePoly(p, x, n, xhat))




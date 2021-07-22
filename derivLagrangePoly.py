# The function will find the  p+1 derivative of Lagrange interpolating polynomials
# given a set of nodal points
# Input: p - integer polynomial degree
#        x - set of p+1 nodal points
#        n - number of points in evaluation vector
#        xhat - set of evaluation points
# Output:LDiff - matrix containing the evaluated derivative of Lagrange polynomials

import numpy as np


def derivLagrangePoly(p, x, n, xhat):
    LDiff = np.zeros((p + 1, n))
    for j in range(p + 1):
        for i in range(p + 1):
            if i != j:
                productTerm = np.ones((1, n))
                for k in range(p + 1):
                    if k != i and k != j:
                        productTerm = productTerm * (xhat - x[k]) / (x[j] - x[k])
                LDiff[j, :] = LDiff[j, :] + productTerm / (x[j] - x[i])

    return LDiff


# Example
# p = 3
# x = np.linspace(-0.5, 0.5, 4)
# n = 6
# xhat = np.linspace(-1, 1, 6)
# print(derivLagrangePoly(p, x, n, xhat))


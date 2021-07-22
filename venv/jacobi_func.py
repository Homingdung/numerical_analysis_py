# The function will perform the Jacobi iteration method
# for the solution of the linear system Ax = b, for Nmax
# iterations
# Input: n by n matrix A
#        n by 1 matrix b
#        n by 1 starting vector x0
# Output: n by (Nmax + 1) matrix containing all iterations


import numpy as np


def jacobi_func(A, b, x0, Nmax):
    x_mat = np.zeros((len(x0), Nmax + 1))
    x_mat[:, 0] = x0.ravel()
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    Dinv = np.diag(1 / np.diag(A))
    T = np.dot(Dinv, (L + U))
    c = np.dot(Dinv, b)
    for i in range(Nmax):
        x_mat[:, i + 1] = np.dot(T, x_mat[:, i]).ravel() + c.ravel()
    return x_mat

# Example
# A = np.array([[2, -1, 1], [1, 2, -1], [1, -1, 2]])
# b = np.array([[-1], [6], [-3]])
# x0 = np.array([[0, 0, 0]]).T
# print(jacobi_func(A, b, x0, 5))

# The function will perform the forward elimination step of Gaussian elimination without
# row exchanges to obtain the echelon form U of A, and in addition computes the
# lower triangular matrix L, so that L * U = A
# Input: n by n matrix A


import numpy as np


def forwElimLU_func(A):
    n = np.size(A, 1)
    a = np.ones(n)
    L = np.diag(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if abs(A[i, i]) < 0.00000008:
                break
            mij = A[j, i] / A[i, i]
            L[j, i] = mij
            A[j, i] = 0
            for k in range(i + 1, n):
                A[j, k] = A[j, k] - mij * A[i, k]
        U = A
    return L, U


# Example
# A = np.array([[1, 2, 3], [4, 5, 6], [2, 4, 6]])
# print(forwElimLU_func(A))



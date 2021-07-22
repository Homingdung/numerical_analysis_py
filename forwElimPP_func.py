# The function will perform the forward Gaussian Elimination and backward substitution
# Input: n by n matrix A
#        n by 1 matrix b
# Output: echelon form of augmented matrix A and solution x

import numpy as np


# A = np.array([[1, 2, 3], [2, 3, 1], [4, 6, 8]])
# b = np.array([[2], [5], [8]])

def forwElimPP_func(A, b):
    n = len(b)
    # forward elimination
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] = A[i, j] - m * A[k, j]
            b[i] = b[i] - m * b[k]
    # backward substitution
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i, j] * x[j]
        x[i] = (b[i] - sum) / A[i, i]
    A = np.c_[A, b]
    return A, x


# Example
# A = np.array([[1, 1, -1], [2, -1, 1], [-1, 2, 2]])
# b = np.array([[-2], [5], [1]])
# print(forwElimPP_func(A, b))

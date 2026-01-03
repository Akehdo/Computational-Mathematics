import numpy as np

def cramer(A: np.ndarray, b: np.ndarray) -> np.ndarray:

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = A.shape[0]

    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square")

    if b.size != n:
        raise ValueError("Vector b must have the same dimension as A")

    D = np.linalg.det(A)

    if np.isclose(D, 0.0):
        raise ValueError("System is singular or not compatible")

    x = np.zeros(n)

    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        D_i = np.linalg.det(A_i)
        x[i] = D_i / D

    return x

A = np.array([
    [2, -1, 3],
    [1,  0, 1],
    [3,  2, 4]
])

b = np.array([5, 2, 10])

x = cramer(A, b)
print(x)
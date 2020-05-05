import numpy as np

A = np.random.random((2, 2))
A += A.T

print(A)

B = np.random.random((2, 2))
B += B.T

print(B)

C = np.dot(A, B)

print(C)

print(np.linalg.eigvals(C))

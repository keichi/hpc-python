import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]], dtype=np.float32)

print(a)

print(a[1, :])

print(a[:, 2])

a[:2, :2] = 0.21

print(a)

a = np.zeros((8, 8))
a[::2, ::2] = 1
a[1::2, 1::2] = 1

print(a)

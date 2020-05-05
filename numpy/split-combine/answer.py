import numpy as np

a = np.arange(64).reshape(8, 8)

b = np.split(a, 2)
print(b)
print(np.concatenate(b))

c = np.split(a, 2, axis=1)
print(c)
print(np.concatenate(c, axis=1))

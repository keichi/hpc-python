import numpy as np

x = np.arange(0, np.pi, 0.1)
y = (np.sin(x[2:]) - np.sin(x[:-2])) / (2 * 0.1)

print(y)
print(y - np.cos(x[1:-1]))

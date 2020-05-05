import numpy as np

for i in range(-1, -7, -1):
    dx = 10 ** i
    x = np.arange(0, np.pi/2, dx)
    S = np.sum(np.sin((x[1:] + x[:-1]) / 2) * dx)
    print(f"dx={dx} S={S}")

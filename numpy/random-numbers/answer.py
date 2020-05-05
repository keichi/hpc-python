import numpy as np
import matplotlib.pyplot as plt

gauss = np.random.normal(0, 1, 1000)

print(np.mean(gauss), np.std(gauss))

unif = np.random.random(1000)

print(np.mean(unif), np.std(unif))

plt.hist(gauss)
plt.show()

plt.hist(unif)
plt.show()

import numpy as np

data = np.loadtxt("xy-coordinates.dat")

data += np.array([0, 2.5])

np.savetxt("xy-coordinates-new.dat", data)

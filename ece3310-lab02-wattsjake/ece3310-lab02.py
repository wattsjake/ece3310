import numpy as np
import matplotlib.pyplot as plt

# number of samples
ns = 1000
lmbda = 1
L = 1 * lmbda
dz = L/ns

gamma = 1

points = np.linspace(0, L, ns)

v = 1 + gamma*np.exp(-1j*2*(2*np.pi/lmbda)*points)

plt.plot(points, v)
plt.show()



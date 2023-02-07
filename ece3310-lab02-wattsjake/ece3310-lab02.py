import numpy as np
import matplotlib.pyplot as plt

# number of samples
ns = 1000
lmbda = 1
L = 1 * lmbda
dz = L/ns

gamma = np.array([1,(1/5),-1])

points = np.linspace(0, L, ns)

plt.grid(True)
plt.title('V_standing R-Term Line, L=1 lambda, Z_0 = 50 ohm')
#turn on legend for each line

plt.xlabel('Lambda (m)')
plt.ylabel('V_standing(V)')
#x axis go in steps of .1
plt.xticks(np.arange(0, 1.1, step=0.1))
#y axis go in steps of .2
plt.yticks(np.arange(0, 2.1, step=0.2))

for value in gamma:
    v = abs(1 + value*np.exp(-1j*2*(2*np.pi/lmbda)*points))
    #turn on grid

    plt.plot(points, v, label='Gamma = ' + str(value))

plt.legend(loc='lower left')
plt.show()



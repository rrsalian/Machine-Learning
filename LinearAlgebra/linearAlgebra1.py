
import numpy as np
import matplotlib.pyplot as plt

soa = np.array([[0, 0, 2, 4], [2, 4, 2, -4], [0, 0, 4, 0]])
X, Y, U, V = zip(*soa)
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
plt.show()

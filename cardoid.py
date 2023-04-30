import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0, 2*np.pi, 1000)
a = 1
r = 2*a * (1.0 + np.cos(theta))
plt.polar(theta, r)
plt.show()

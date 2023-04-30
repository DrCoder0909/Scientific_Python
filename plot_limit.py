import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0., 2., 1000)
f = t*np.exp(t+np.sin(20*t))
plt.plot(t, f)

plt.show()

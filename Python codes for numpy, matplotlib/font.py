import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(.1, 1., 100)
yi = 1./x
ye = 10.*np.exp(-2*x)
plt.plot(x, yi, color="tab:blue", label="inverse function",
         linestyle="--", linewidth=0.5, marker="^")
plt.plot(x, ye, color="#ff00ff", label=" exponential function",
         linestyle="--", linewidth=0.5, marker="+")
plt.legend(loc="best")

plt.show()

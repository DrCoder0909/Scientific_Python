import numpy as np
import matplotlib.pyplot as plt

fig , ax = plt.subplots()
ax.axis("equal")

y = np.linspace(-1,1,100)
xmax= np.sqrt(1- y**2)
ax.hlines(y, -xmax, xmax, color = "g")

ax.vlines(-1, -1, 1 , lw =2, color ="r")
ax.vlines(1,-1,1, lw =2, color ="r")
ax.hlines(-1,-1,1, lw=2 , color ="r")
ax.hlines(1, -1, 1, lw=2, color = "r")
ax.vlines(y[::10], -1, 1, color ="b")

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

plt.show()

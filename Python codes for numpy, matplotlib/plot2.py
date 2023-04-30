import random
import matplotlib.pyplot as plt
ax, ay= [],[]
for i in range(100):
    ax.append(random.random())
    ay.append(random.random())

plt.scatter(ax,ay)
plt.show()
plt.savefig("plot.pdf")

import math
import matplotlib.pyplot as plt
xmin, xmax = -2.0* math.pi , 2.0* math.pi
n=1000
ax=[0.0]*n
ay=[0.0]*n
dx= (xmax-xmin)/(n-1)
for i in range(n):
    xpt=xmin+ i*dx
    ax[i]=xpt
    ay[i]=math.sin(xpt)**2

plt.plot(ax,ay)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
n=1000
xmin,xmax=-2*np.pi , 2*np.pi
x=np.linspace(xmin,xmax,n)
y1=np.sin(x)**2
y2=np.cos(x)**2

plt.plot(x,y1,label="sin^2(x)")
plt.legend("lower right")

plt.plot(x,y2)
plt.show()

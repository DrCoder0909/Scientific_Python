import numpy as np
import matplotlib.pyplot as plt
n=1000
xmin, xmax= -2*np.pi, 2*np.pi
x= np.linspace(xmin,xmax,n)
y=np.sin(x)**2
plt.plot(x,y)
plt.show()

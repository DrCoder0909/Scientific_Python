import numpy as np 
import matplotlib.pyplot as plt

x, y = np.loadtxt(fname = "naca-4412.txt", skiprows = 1, usecols = (2,3), unpack = True)
plt.plot(x,y)
plt.show()
print(np.where(x==1000))
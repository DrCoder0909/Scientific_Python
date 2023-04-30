# Creates  a vector contour field
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

X = np.linspace(0,1,100)
Y = X.copy()
X,Y = np.meshgrid(X,Y)
alpha = np.radians(25)
cX, cY = 0.5, 0.5
sigX, sigY = 0.2, 0.3
rX= np.cos(alpha)*(X-cX)- np.sin(alpha)*(Y-cY)+cX
rY= np.sin(alpha)*(X-cX)+ np.cos(alpha)*(Y-cY)+cY

Z = (rX-cX)* np.exp(-((rX-cX)/sigX)**2)* np.exp(-((rY-cY)/sigY)**2)
fig = plt.figure()
ax = fig.add_subplot()

cpf = ax.contourf(X, Y, Z, 20, cmap = cm.Greys)
colors = ["w" if level>0 else "k" for level in cpf.levels]
cp= ax.contour(X, Y, Z, 20, colors = colors)
ax.clabel(cp, fontsize =12, colors= colors)
plt.show()

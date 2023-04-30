import numpy as np
import matplotlib.pyplot as plt

#Dipole charge (C), permittivity of free space(F.m-1)
q , eps0 = 1.602e-19, 8.854e-12
#Dipole +q, -q distance(m) and a convenient combination of parameters.
d = 1.e-12
k = 1/4/np.pi/eps0*q*d

#Casterian axis system with origin at the dipole (m)
X = np.linspace(-5e-11, 5e-11, 1000)
Y =  X.copy()
X, Y = np.meshgrid(X,Y)

#Dipole electrostatic potential (V), using point dipole approximation
phi = k*X/ np.hypot(X,Y)**3

fig , ax = plt.subplots()
#Draw contours at value of phi given by levels
levels = np.array([10**pw for pw in np.linspace(0,5,20)])
levels = sorted(list(-levels)+ list(levels))
#Monochrome plot of potential
ax.contour(X, Y , phi, levels = levels, linewidths = 2)
plt.show()

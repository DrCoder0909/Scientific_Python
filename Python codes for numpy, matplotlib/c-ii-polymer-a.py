import matplotlib.pyplot as plt
from polymer import Polymer
import numpy as np
pi = np.pi

Np =3000
N,a = 1000, 1
R = [None]*Np
for i in range(Np):
    polymer = Polymer(N,a)
    Rx, Ry, Rz = polymer.R
    R[i] = np.sqrt(Rx**2 + Ry**2+ Rz**2)
    if not (i+1)%100:
        print(i+1, "/", Np)

plt.hist(R, 50 ,density = True )

r = np.linspace(0,200,1000)
msr = N*a**2
Pr = 4*pi*r**2*(2*pi*msr/3)**-1.5* np.exp(-3*r**2/2/msr)
plt.plot(r,Pr, lw = 2, c = "r")
plt.xlabel("R")
plt.ylabel("P(R)")
plt.show()

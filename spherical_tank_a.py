import numpy as np
import matplotlib.pyplot as plt
Polynomial = np.polynomial.Polynomial

#Radius of the spherical tank in m.
R = 1.5
#Flow rate out of the tank. m^3.s-1
F = 2.e-4
# Total volume of tank
V0 = 4/3 *np.pi* R**3
#Total time taken for the tank to empty
T = V0/F

#Coefficients of the quadratic and cubic terms
#of p(h), the polynomial to be solved for h
c2 , c3 = np.pi*R , -np.pi/3

N= 100
#Array of N time points between 0 and T inclusive.
time = np.linspace(0,T,N)
#create the corresponding array of heights h(t).
h = np.zeros(N)
for i , t in enumerate(time):
    c0 = F*t -V0
    p = Polynomial([c0 , 0 , c2, c3])
    #Find the three roots of this polynomial.
    roots = p.roots()
    print(roots)
    #We want the root for which 0 <= h <= 2R
    h[i] = roots[(0<= roots) & (roots <= 2*R)][0]
print(h)
print(type(roots))

plt.plot(time , h , "o")
plt.xlabel("Time/s")
plt.ylabel("Height in tank/m")
plt.show()

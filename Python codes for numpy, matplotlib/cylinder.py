# -*- coding: utf-8 -*-
"""
Created on Thu May 19 07:44:16 2022

@author: ayush
"""

#Flow over a cylinder

import numpy as np
import matplotlib.pyplot as plt

#velocity of free stream(m/s)
vel = np.array([0, 1.98, 2.80, 3.70, 4.64, 5.42])
rho = 1.225 #kgm^-3
mu =1.789* 10**(-5)
d = 0.07 #m
Reynolds_num = vel*rho*d/mu
rey = np.array(((Reynolds_num[:2]), (Reynolds_num[2:4]), (Reynolds_num[4:])))


#putting in all the values of acquired pressure probes
r1 = (81 ,83, 87, 85, 87, 84, 88, 85, 85, 85, 82)
r2 = (84, 85, 86, 88, 90, 87, 90, 89, 90, 89, 87)
r3 = (84, 85, 87.5, 88, 89, 86, 90, 87, 88, 90, 89.5)
r4 = (83.5, 85, 87, 88.5, 89, 86.5, 90, 88.5, 88.5, 89.5, 89.5)
r5 = (83.5, 85, 86, 88.5, 88, 86, 89.5, 87.5, 87, 89,89.5)
r6 = (88, 89.5, 87.5, 88.5, 89, 86, 89, 87.5, 87.5, 88.5, 87)


#color chart to use
colors= np.array([["#1745F0","#F0172E"],["#04C61C","#7510EE"],["#EE3F10", "#4B4902"]])


r = np.array(((r1,r2),(r3,r4),(r5,r6)), dtype = "object")
r_con = np.concatenate((r1,r2,r3,r4,r5,r6))

#maximum value of pressure among all
max = np.amax(r_con)
print(r_con)

fig, axes = plt.subplots(nrows = 3, ncols = 2, figsize = (20,20), dpi =1200)

x= np.linspace(0, 2*np.pi, 12)
x =np.delete(x, 11)
print(x)

for i in (0,1):
    for j in (0,1,2):
        ax = axes[j,i]
        ax.plot(x,r[j,i],colors[j,i], ls = "-")
        ax.set_ylim(np.amin(r_con), np.amax(r_con))
        ax.set_xticklabels(("$0$", "$\pi/6$", "$\pi/3$","$\pi/2$", "$2\pi/3$", "$5\pi/6$",
                          "$\pi$","$7\pi/6$", "$4\pi/3$", "$3\pi/2$", "$5\pi/3$"), rotation =90)
        ax.set_xlabel("Angle along the cylinder")
        ax.set_ylabel("Pressure sensed using the probe")
        ax.set_title("Re = {}".format(rey[j,i]))
        ax.grid("True")


fig.tight_layout()        
plt.show()
plt.savefig("cylinder_wind_tunnel.jpg")

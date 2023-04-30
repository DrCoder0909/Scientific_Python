import numpy as np
import matplotlib.pyplot as plt
import xlrd
from itertools import permutations
import scipy as sp
from scipy.integrate import quad


wb = xlrd.open_workbook("naca_0012_re.xls")
sheet= wb.sheet_by_index(1)
airfoil = np.zeros((2,200))

for i in range(sheet.ncols):
    airfoil[i,]=sheet.col_values(i)
print(airfoil)

fig = plt.figure()
ax1= fig.add_subplot()
plt.plot(airfoil[0], airfoil[1])
#plt.show()

x_panel = []
for i in airfoil[0,::10]:
    x_panel.append(i)
print(x_panel)

y_panel= []
for i in airfoil[1,::10]:
    y_panel.append(i)
print(y_panel)

ax2= fig.add_subplot()
plt.plot(x_panel, y_panel)
plt.show()

panel_num = 0
const = np.zeros((len(x_panel), len(x_panel)))
i_panels =[]
j_panels = []

panel = np.array((x_panel,y_panel))
panel_division = permutations(range(len(x_panel)-1),2)
for ith,jth in panel_division:
    i_panels.append(ith), j_panels.append(jth)

for i in range(len(x_panel)):
    if i < len(x_panel)-2:
        for j in range(len(x_panel)):
            try:
                x_i = panel[0,i]
                y_i = panel[1,i]
                x_i2= panel[0,i+1]
                y_i2 = panel[1,i+1]

                x_j , y_j = panel[:,j]
                x_j2, y_j2 = panel[:,j+1]
            except IndexError:
                X_i = panel[0,i]
                y_i = panel[1,i]
                x_i2= panel[0,i+1]
                y_i2 = panel[1,i+1]

                x_j , y_j = panel[:,j]
                x_j2, y_j2 = panel[:,0]
 #Condition 1
        if (y_i2-y_i)<0 and (x_i2-x_i)>0:
            phi_i = np.pi*3/2 + np.pi/2 + np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)<0 and (x_j2-x_j)>0:
            phi_j = np.pi*3/2 + np.pi/2 + np.arctan((y_j2-y_j)/(x_j2-x_j))

#Condition 2
        if (y_i2-y_i)>0 and (x_i2-x_i)>0:
            phi_i = np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)>0 and (x_j2-x_j)>0:
            phi_j =np.arctan((y_j2-y_j)/(x_j2-x_j))

#Condition 3
        if (y_i2-y_i)>0 and (x_i2-x_i)<0:
            phi_i =np.pi + np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)>0 and (x_j2-x_j)<0:
            phi_j =np.pi+ np.arctan((y_j2-y_j)/(x_j2-x_j))

#Condition 4
        if (y_i2-y_i)<0 and (x_i2-x_i)<0:
            phi_i = np.pi*3/2 -  np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)<0 and (x_j2-x_j)<0:
            phi_j = np.pi*3/2 -  np.arctan((y_j2-y_j)/(x_j2-x_j))

        cp_i = panel[:,i+1]- panel[:,i]
        cp_i = cp_i/2
        cp_x= cp_i[0]
        cp_y=cp_i[1]

        #defining all the constants of integration

        A = -(cp_x-x_j)*np.cos(phi_j) - (cp_y- y_j)*np.sin(phi_j)
        B= (cp_x- x_j)**2 + (cp_y - y_j)**2
        C = np.sin(phi_i - phi_j)
        D = (cp_y -y_j)*np.cos(phi_i)-(cp_x-x_j)*np.sin(phi_i)
        S_j = np.sqrt((x_j2-x_j)**2 + (y_j2-y_j)**2)
        E = np.sqrt(B-A**2)

       #Integrating
        Integrated = (C/2)*np.log((S_j**2 + 2*A*S_j+ B)/B)+ ((D- A*C)/E)*(np.arctan((S_j+A)/E)- np.arctan(A/E))

        const[i,j]= Integrated/ np.pi
        const[i,i]= 1/2

    if i == len(x_panel)-1:
        for j in range(len(x_panel)):
            try:
                X_i = panel[0,i]
                y_i = panel[1,i]
                x_i2= panel[0,0]
                y_i2 = panel[1,0]

                x_j , y_j = panel[:,j]
                x_j2, y_j2 = panel[:,j+1]
                
            except IndexError:
                X_i = panel[0,i]
                y_i = panel[1,i]
                x_i2= panel[0,i+1]
                y_i2 = panel[1,i+1]

                x_j , y_j = panel[:,j]
                x_j2, y_j2 = panel[:,0]

        if (y_i2-y_i)<0 and (x_i2-x_i)>0:
            phi_i = np.pi*3/2 + np.pi/2 + np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)<0 and (x_j2-x_j)>0:
            phi_j = np.pi*3/2 + np.pi/2 + np.arctan((y_j2-y_j)/(x_j2-x_j))

        if (y_i2-y_i)>0 and (x_i2-x_i)>0:
            phi_i = np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)>0 and (x_j2-x_j)>0:
            phi_j =np.arctan((y_j2-y_j)/(x_j2-x_j))

        if (y_i2-y_i)>0 and (x_i2-x_i)<0:
            phi_i =np.pi + np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)>0 and (x_j2-x_j)<0:
            phi_j =np.pi+ np.arctan((y_j2-y_j)/(x_j2-x_j))

        if (y_i2-y_i)<0 and (x_i2-x_i)<0:
            phi_i = np.pi*3/2 -  np.arctan((y_i2-y_i)/(x_i2-x_i))

        if (y_j2-y_j)<0 and (x_j2-x_j)<0:
            phi_j = np.pi*3/2 -  np.arctan((y_j2-y_j)/(x_j2-x_j))

        cp_i = panel[:,0]- panel[:,i]
        cp_i = cp_i/2
        cp_x= cp_i[0]
        cp_y=cp_i[1]

        #defining all the constants of integration

        A = -(cp_x-x_j)*np.cos(phi_j) - (cp_y- y_j)*np.sin(phi_j)
        B= (cp_x- x_j)**2 + (cp_y - y_j)**2
        C = np.sin(phi_i - phi_j)
        D = (cp_y -y_j)*np.cos(phi_i)-(cp_x-x_j)*np.sin(phi_i)
        S_j = np.sqrt((x_j2-x_j)**2 + (y_j2-y_j)**2)
        E = np.sqrt(B-A**2)

       #Integrating
        Integrated = C/2*np.log((S_j**2 + 2*A*S_j+ B)/B)+ ((D- A*C)/E)(np.arctan((S_j+A)/E)- np.arctan(A/E))

        const[i,j]= Integrated/ np.pi

print(const)

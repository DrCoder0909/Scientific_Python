import numpy as npA
import matplotlib.pyplot as plt
import xlrd

wb = xlrd.open_workbook("naca_0012.xls")
sheet = wb.sheet_by_index(1)
airfoil= np.zeros((2,201))
print(airfoil)
for i in range(sheet.ncols):
    airfoil[i,]=sheet.col_values(i)
print(airfoil)
print(type(airfoil))

fig , ax = plt.subplots()
plt.plot(airfoil[0], airfoil[1])
plt.show()

import numpy as np
import matplotlib.pyplot as plt

dt = np.dtype([("month", np.int), ("day", np.int), ("T", np.float)])
data= np.genfromtxt("boston2019.dat",dtype = dt, usecols =(1,2,3), delimiter =(4,2,2,6))

heatmap= np.empty((12,31))
heatmap[:]= np.nan
for month , day , T in data:
    heatmap[month-1, day-1]= T

fig = plt.figure()
ax = fig.add_subplot()
im = ax.imshow(heatmap, interpolation ="nearest")
ax.set_yticks(range(12))
ax.set_yticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                    "Aug", "Sep", "Oct", "Nov", "Dec"])

days= np.array(range(0,31,2))
ax.set_xticks(days)
ax.set_xticklabels(["{:d}".format(day+1) for day in days])
ax.set_xlabel("Day of month")
ax.set_title("Maximum daily temperature in Boston , 2019")

cbar = fig.colorbar(ax =ax, mappable= im, orientation = "horizontal")
cbar.set_label("Temperature, $^\circ\mathrm{C}$")
plt.show()

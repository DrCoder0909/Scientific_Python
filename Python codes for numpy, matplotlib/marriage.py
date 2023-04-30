import numpy as np
import matplotlib.pyplot as plt

year , age_m , age_f = np.loadtxt("marriage.txt", unpack = True , skiprows = 3)
fig , ax = plt.subplots()
#plot ages with male or female symbols as markers
ax.plot(year, age_m , marker ="$\u2642$" , markersize = 14 , c = "blue", lw = 2,
        mfc= "blue", mec ="blue")

ax.plot(year, age_f , marker ="$\u2640$" , markersize =14 , c ="magenta", lw=2,
        mfc = "magenta", mec ="magenta")
ax.grid()

ax.set_xlabel("Year")
ax.set_ylabel("Age")
ax.set_title("Median age at first marriage in the USA, 1890-2010")

plt.show()

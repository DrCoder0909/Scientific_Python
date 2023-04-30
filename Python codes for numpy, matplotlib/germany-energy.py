import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("energy.txt", skiprows = 2, dtype = "f8")
years = data[:,0]
n = len(years)

#Gwh to Twh
data[:,1] /=1000

fig = plt.figure()
ax = fig.add_subplot(111)
sources = ("Hydroelectric", "Wind", "Biomass", "Photovoltaics")
hatch = ["oo", " ", "xxxx" , "//"]
bottom = np.zeros(n)
bars = [None]*len(sources)

for i, source in enumerate(sources):
	bars[i]= ax.bar(years, bottom = bottom , height = data[:, i+1],
		color = "w", hatch = hatch[i], align = "center", edgecolor = "k")
	bottom += data[:, i+1]

ax.set_xticks(years[::2])
plt.xticks(rotation =90)
ax.set_xlim(1989,2019)
ax.set_ylabel("Renewable Electricity(TWh)")
ax.set_title("Renewable Electricity generation in Germany, 1990-2018")
plt.legend(bars, sources, loc = "best")
print(bars)
plt.show()

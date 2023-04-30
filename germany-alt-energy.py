import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("germany-energy-sources.txt", skiprows = 2, dtype = "f8")
#converters, unpack, comments
years = data[:,0]
print(type(years))
n = len(years)

#GWh to TWh
data[:,1] /=1000

fig , ax = plt.subplots()
sources = ("Hydroelectric", "Wind" , "Biomass" , "Photovoltaics")
hatch = ["oo", " ", "xxx", "//"]
bottom = np.zeros(n)
bars= [None]*4
for i, sources in enumerate(sources):
    bars[i] = ax.bar(years, bottom = bottom , height=data[:, i+1], color = "w",
                    hatch = hatch[i], align = "center", edgecolor ="k")
    bottom += data[:, i+1]
print(bars)
ax.set_xticks(years[::2])
plt.xticks(rotation =90)
ax.set_xlim(1989,2019)
ax.set_ylabel("Renewable energy(TWh)")
ax.set_title("Renewable electricity generation in Germany, 1990-2018")
plt.legend(bars, sources, loc = "upper left")
plt.show()

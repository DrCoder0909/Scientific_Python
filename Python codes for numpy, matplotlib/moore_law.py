# moore.py
import numpy as np
import matplotlib.pyplot as plt

year = [1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000, 2003,
        2004, 2007, 2008, 2012]
ntrans = ([0.0025, 0.005, 0.029, 0.12, 0.275, 1.18, 3.1, 7.5, 24.0, 42.0, 220.0,
           592.0, 1720.0, 2046.0, 3100.0])

y0, n0 = year[0], ntrans[0]

y = np.linspace(y0, year[-1], year[-1]-y0+1)
print(y)
print(len(y))

T2 = 2

moore = np.log10(n0) + (y-y0) / T2 * np.log10(2)
print(moore)
print(len(moore))

plt.plot(year, np.log10(ntrans), "*", linestyle=":", markersize=12, color="r",
         markeredgecolor="r", label="observed")

plt.plot(y, moore, linewidth=2, color="k", linestyle="--", label="predicted")

plt.legend(fontsize=16, loc="upper left")

plt.xlabel("Year")
plt.ylabel("log(ntrans)")
plt.title("Moore's law")
plt.show()

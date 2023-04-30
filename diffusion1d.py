import numpy as np
import matplotlib.pyplot as plt


A , H = 1.e-4, 1.e3
theta0= 300

metals = np.array([("Cu", 3.45e7, 1.11e-4), ("Fe", 3.50e7, 2.35e-5)],
                   dtype=[("symbol", "|S2"), ("cp", "f8"), ("D", "f8")])

xlim , nx = 0.05, 1000
x = np.linspace(-xlim, xlim , nx)

times = (1e-2, 0.1, 1)
fig , axes = plt.subplots(nrows = 3, ncols =2 , figsize =(7,8))
for j , t in enumerate(times):
    for i , metal in enumerate(metals):
        print(metal)
        print(type(metal))
        symbol, cp1, D = metal
        ax = axes[j,i]
        theta = theta0 + H/cp1/A/np.sqrt(D*t*4*np.pi)*np.exp(-x**2/4/D/t)
        ax.plot(x*100, theta , "k")
        ax.set_title("{}, $t = {}$ s".format(symbol.decode("utf8"), t))
        ax.set_xlim(-4,4)
        ax.set_xlabel("$x\;\mathrm{cm}$")
        ax.set_ylabel("$\Theta\;/\mathrm{k}$")

for j in (0,1,2):
    ymax = max(axes[j,0].get_ylim()[1], axes[j,1].get_ylim()[1])
    print(axes[j,0].get_ylim(), axes[j,1].get_ylim())
    for i in (0,1):
        ax = axes[j,i]
        ax.set_ylim(theta0 , ymax)
        ax.set_yticks([theta0, (ymax+theta0)/2, ymax])
fig.tight_layout()
plt.show()

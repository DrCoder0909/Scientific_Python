import numpy as np
import matplotlib.pyplot as plt

#the initial value of y at t =0, lifetime(s)
N, tau = 10000,28
#Maximum time to consider(s)
tmax = 100
#A suitable grid of time points  and the exponential decay itself
t= np.linspace(0,tmax,1000)
y = N*np.exp(-t/tau)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,y, ls = "-", lw=0.5, c= "red")

#the number of lifetimes that fall within the plotted time interval
ntau = (tmax//tau)+1
#xticks at 0, tau , 2*tau,....., ntau*tau; yticks at the corresponding y values
xticks= [i*tau for i in range (ntau)]
yticks = [N*np.exp(-i) for i in range(ntau)]
ax.set_xticks(xticks)
ax.set_yticks(yticks)

#xticks labels = 0 , tau, 2tau
xtick_labels = [r"$0$", r"$\tau$"] + [r"${}\tau$".format(k) for k in range(2, ntau)]
ax.set_xticklabels(xtick_labels)

ytick_labels = [r"$N$", r"$N/e$"] + [r"$N/{}e$".format(k) for k in range (2, ntau)]
ax.set_yticklabels(ytick_labels)

ax.set_xlabel(r"$t\;/\mathrm{s}$")
ax.set_ylabel(r"$y$")
ax.grid()


ax.set_xticklabels([])
ax.set_yticklabels([])
plt.show()

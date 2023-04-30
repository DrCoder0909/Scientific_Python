import numpy as np
import matplotlib.pyplot as plt

nrows = 10
fig, axes = plt.subplots(nrows, 1)
fig.subplots_adjust(hspace = 0)

x = np.linspace(0,1,1000)

for i in range(nrows):
	n = nrows - i 
	axes[i].plot(x, np.sin(n*np.pi* x), "tab:blue", lw =2)
	axes[i].xaxis.set_ticks_position("bottom")
	axes[i].tick_params(axis = "both", direction = "in", color = "red", labelcolor = "tab:pink")
	if i <nrows -1:
		axes[i].set_xticks(np.arange(0,1,1/n))
		axes[i].set_xticklabels("")
	axes[i].set_yticklabels("")
plt.show()
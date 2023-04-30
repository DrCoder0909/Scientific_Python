import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

a = np.eye(10,10)
a+= a[::-1,:]

fig = plt.figure()
ax1= fig.add_subplot(121)
ax1.imshow(a, interpolation = "bilinear", cmap= cm.Greys_r)

ax2= fig.add_subplot(122)
ax2.imshow(a, cmap =cm.Greys_r)

plt.show()

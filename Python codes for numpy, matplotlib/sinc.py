import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-20,20,1001)
y=np.sin(x)/x

plt.plot(x,y)
plt.show()

print(y[498:503])

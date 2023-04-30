import matplotlib.pyplot as plt
import numpy as np
plt.rc("text", usetex= "True")

x= np.linspace(-10,10,1001)
for n in range(1,5):
    y=x**n*np.sin(x)
    y/=max(y)
    plt.plot(x,y, label= r'$x^{}\ sin x$'.format(n))
plt.legend(loc="lower center")
plt.show()

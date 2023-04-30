import numpy as np
import matplotlib.pyplot as plt

def gain(d,w):
    """Return the power as a function of azimuthal angel, phi."""
    phi = np.linspace(0, 2*np.pi, 1000)
    psi = 2*np.pi*d/lam*np.cos(phi)
    print(psi)
    j = np.arange(len(w))
    A =np.sum(w[j]* np.exp(j*1j*psi[:, None]), axis =1)
    print(A)
    g = np.abs(A)**2
    print(g)
    return phi , g

def get_directive_gain(g , minDdBi = -20):
    """Return the "directive Gain" of the antenna array producing gain g."""
    DdBi = 10*np.log10(g/np.max(g))
    return np.clip(DdBi, minDdBi, None)

lam =1
d = lam/2
w = np.array([1,-1,1])
#calculate gain and directive gain; plot on a polar chart
phi,g =gain(d,w)
DdBi = get_directive_gain(g)

fig = plt.figure()
ax = fig.add_subplot(projection = "polar")
ax.plot(phi, DdBi)
ax.set_rticks([-20, -15, -10, -5])
ax.set_rlabel_position(45)
plt.show()

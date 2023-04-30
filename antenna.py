import numpy as np
import matplotlib.pyplot as plt

def gain(d , w):
    """return the power as a function of azimuthal angle, phi"""
    phi = np.linspace(0, 2*np.pi, 1000)
    psi = 2*np.pi*d/lam*np.cos(phi)
    print(psi)
    A = w[0] + w[1]*np.exp(1j*psi)
    print(A)
    g = np.abs(A)**2
    return phi, g

def get_directive_gain(g , minDdBi = -20):
    """ Return the "directive gain" of the antenna array producing gain g."""
    DdBi= 10*np.log10(g/np.max(g))
    return np.clip(DdBi , minDdBi, None)
    #return DdBi

#wavelength, antenna spacing , feed coefficient
lam = 1
d = lam
w = np.array([1, -1j])
#Calculate the gain and directive gain, plot on a polar chart
phi, g = gain(d,w)
DdBi = get_directive_gain(g)

plt.polar(phi, DdBi)
ax = plt.gca()
ax.set_rticks([-20, -15, -10,-5])
#ax.set_xticklabels("Helo")
ax.set_rlabel_position(45)
plt.show()

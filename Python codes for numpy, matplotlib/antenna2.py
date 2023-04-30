import numpy as np
import matplotlib.pyplot as plt

def gain(d,w):
	"""Returns the power as a function of Azimuthal angle , phi"""
	phi = np.linspace(0, 2*np.pi, 1000)
	psi = 2*np.pi *d/lam*np.cos(phi)
	j = np.arange(len(w))
	A = np.sum(w[j]*np.exp(j * 1j * psi[:,None]), axis = 1)
	B = w[j]*np.exp(j * 1j * psi[:,None])
	print(j)
	print("The vale of B is: ",B)
	print("The value of A is:",A)
	g = np.abs(A)**2
	return phi, g

def get_directive_gain(g, minDdBi = -20):
	""" Return the directive gain of the antenna array producing gain g."""
	DdBi = 10*np.log10(g/np.max(g))
	return np.clip(DdBi, minDdBi, None)

lam =1
d = lam/2
w = np.array([1,-1,1])
phi, g = gain(d,w)
DdBi = get_directive_gain(g)

fig = plt.figure()
ax = fig.add_subplot(projection = "polar")
ax.plot(phi, DdBi)
ax.set_rticks([-20,-15,-10,-5])
ax.set_rlabel_position(45)
plt.show()




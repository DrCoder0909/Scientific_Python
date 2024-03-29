import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

FEMALE, MALE = 0,1
dt = np.dtype([("mass", "f8"), ("height", "f8"), ("gender", "i2")])
data = np.loadtxt("body.dat.txt", usecols =(22,23,24), dtype =dt)

fig , ax = plt.subplots()

def get_cov_ellipse(cov, center, nstd, **kwargs):
    """
    Return a matplotlib Ellipse patch representing the covariance matrix cov
    centered at the center and scaled by the factor nstd
    """

    #Find and sort eigrnvalues and eigenvectors into descending order
    eigvals, eigvecs = np.linalg.eigh(cov)
    print(eigvals)
    print(eigvecs)
    order = eigvals.argsort()[::1]
    print(order)
    eigvals, eigvecs = eigvals[order], eigvecs[:,order]
    print(eigvecs)

    #The counterclockwise angle to rotate our ellipse by.
    vx, vy = eigvecs[:,0][0], eigvecs[:,0][1]
    theta = np.arctan2(vy,vx)

    #width and height of ellipse to draw.
    width, height = 2* nstd *np.sqrt(eigvals)
    return Ellipse(xy = center, width =width, height = height,
                   angle = np.degrees(theta), **kwargs)

labels, colors = ["Female", "Male"], ["magenta", "blue"]
for gender in(FEMALE, MALE):
    sdata= data[data["gender"]==gender]
    height_mean = np.mean(sdata["height"])
    mass_mean = np.mean(sdata["mass"])
    cov = np.cov(sdata["mass"], sdata["height"])
    ax.scatter(sdata["height"], sdata["mass"], color = colors[gender],
               label = labels[gender])
    e = get_cov_ellipse(cov, (height_mean, mass_mean),3,fc = colors[gender], alpha= 0.4)
    ax.add_patch(e)

ax.set_xlim(140,210)
ax.set_ylim(30,120)
ax.set_xlabel("height/cm")
ax.set_ylabel("mass/kg")
ax.legend(loc = "upper left", scatterpoints=1)
plt.show()

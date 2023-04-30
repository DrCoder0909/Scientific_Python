import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

dt, tmax = 0.01, 5
f, alpha = 2.5, 1
t, M = [], []

fig, ax = plt.subplots()
line, = ax.plot([],[])
ax.set_xlim(0, tmax)
ax.set_ylim(-1,1)
ax.set_xlabel("t/s")
ax.set_ylabel("M(arb.units)")

def animate(i):
    """Draw the frame i of the animation"""

    global t, M
    _t = i*dt
    t.append(_t)
    M.append(np.sin(2*np.pi*f*_t)*np.exp(-alpha*_t))
    line.set_data(t,M)

interval , nframes = 1000*dt, int(tmax/dt)
ani = animation.FuncAnimation(fig, animate, frames = nframes, repeat =False,
                             interval = interval)
print(ani)
plt.show()

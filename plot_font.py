import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0.0, 0.1, 1000)
Vp_uk, Vp_us= 230* np.sqrt(2), 120*np.sqrt(2)
f_uk, f_us = 50, 60
V_uk= Vp_uk* np.sin(2*np.pi*f_uk*t)
V_us= Vp_us*np.sin(2*np.pi*f_us*t)
plt.plot(t*1000, V_uk , label="UK")
plt.plot(t*1000, V_us, label="US")
plt.title("A comparison of AC voltages in the UK and US")
plt.xlabel(" Time/ms", fontsize=16)
plt.ylabel("Voltage/V", fontsize=16)
plt.legend()
plt.show()

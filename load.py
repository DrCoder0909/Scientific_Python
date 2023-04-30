import numpy as np

arr = np.getfromtxt("14C-sim.csv", skip_header = 2,
                     dtype=[("timestep", "f8"), ("sim1","f8" )],
                      usecols=(1,3), delimiter=" ,")

print(arr)

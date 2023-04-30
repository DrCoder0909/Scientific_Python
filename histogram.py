import matplotlib.pyplot as plt
import random
data = []
for i in range(5000):
    data.append(random.normalvariate(0, 2))
plt.hist(data, density=True)
plt.show()

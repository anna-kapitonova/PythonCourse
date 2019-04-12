import numpy as np
s = np.random.poisson(5, 5000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 15, density=True)
plt.show()

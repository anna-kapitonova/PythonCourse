import numpy as np
s = np.random.pareto(5, 10000)
import matplotlib.pyplot as plt
count, bins, _ = plt.hist(s, 100, density=True)
plt.show()

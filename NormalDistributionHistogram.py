import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(55.0,26.0,100000)
plt.hist(x,100)
plt.show()
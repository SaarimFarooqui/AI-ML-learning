import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.uniform(1,10,100)
plt.hist(numbers)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

randomNumbers =  np.random.uniform(1,10,1000)
mynumbers = [1,2,3,1,2,3,1,2,3,1,2,3,4,4]
plt.hist(mynumbers,3)
plt.show()
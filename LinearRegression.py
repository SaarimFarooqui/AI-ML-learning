import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5,10,100)
y = np.random.normal(1,15,100)

plt.scatter(x,y)
plt.show()
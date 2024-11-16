import numpy as np
from scipy import stats
speed = [90,91,92,95,90,89,87,88,92,93,95,94,96,91,90,87,88,89,90,91,95,94,88,86,89,90]
Mean = np.mean(speed)
Median = np.median(speed)
Mode = stats.mode(speed)

print("The average of all speeds is ", Mean)
print("The center most value of all speeds is ", Median)
print("The most repeated value of all speeds is ", Mode)




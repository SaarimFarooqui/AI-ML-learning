import numpy as np
from scipy import stats
speed = [12,14,12,13,15,11,12,13,14,12,11,11,15,15,14,14,13,12]

average =  np.mean(speed)
middle_value = np.median(speed)
most_repeated = stats.mode(speed)

print("Mean: ", average, "Median: ", middle_value, "Mode: ", most_repeated)
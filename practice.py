import numpy as np
import matplotlib.pyplot as plt

ages = [9,9,9,9,11,12,13,14,15,11,12,13,14,10,9,11,12,13,14,12,11,13,14]
percentile = 50
value = np.percentile(ages, 50)
print(f"The { percentile }% of data falls under the value: ",value)


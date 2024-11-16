import numpy as np

speed = [10,11,12,13,9,8,9,10,11,12,9,10,11,8,9,11,12]
sd = np.std(speed)
var = np.var(speed)
print("The Standard deviation is found to be : ", sd, " and variance is ", var)
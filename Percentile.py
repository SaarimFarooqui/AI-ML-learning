import numpy as np
import pandas as pd
marks = [88,90,77,76,75,44,54,56,65,89,91,73,72,67]
percentile_20 = np.percentile(marks,20)

print("The number greater than 20 percent of all the numbers is : ",percentile_20)

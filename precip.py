import numpy as np
with open("precip_data.txt") as rawdata:
    arr = np.genfromtxt(rawdata)
    precipdat = arr[1:, 2]

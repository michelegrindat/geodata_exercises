import numpy as np
from precip import precipdat
print("The Station of ‘AMW‘ provides daily precipitation values for a total of {} days.".format(str(np.size(precipdat))))
print("Minimum precipitation: " + str(np.min(precipdat)))
print("Maximum precipitation: " + str(np.max(precipdat)))
print("Mean precipitation: " + str(round(np.mean(precipdat), 1)))
import numpy as np

a = np.array(list(map(float, input().split())))
np.set_printoptions(legacy='1.13')
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

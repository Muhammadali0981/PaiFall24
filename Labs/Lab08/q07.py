import numpy as np
from numpy import random

mat = np.random.rand(1000)
print(mat)

mean = np.mean(mat)
var = np.var(mat)
std = np.std(mat)

f = open('data.txt', 'w')
f.write(str(mean))
f.write("\n")
f.write(str(var))
f.write("\n")
f.write(str(std))
f.close()
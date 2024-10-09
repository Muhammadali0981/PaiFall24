import numpy as np
from numpy import random

mat_a = np.random.randint(1, 100, size= (5, 3))
mat_b = np.random.randint(1, 100, size= (3, 2))

result = np.dot(mat_a, mat_b)

print(result)
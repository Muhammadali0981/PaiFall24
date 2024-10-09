import numpy as np
from numpy import random

random_nums = random.choice([2,5,9,10], size= (4,4))
print(random_nums)

result = np.dot(random_nums, np.eye(4, 4))
print(result)

odd_nums = np.arange(3, 34, 2).reshape(4, 4)
print(odd_nums)

print(np.add(result, odd_nums))


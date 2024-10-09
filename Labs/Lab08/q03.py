import numpy as np

nums = np.arange(2, 20, 2).reshape(3, 3)
result = np.multiply(nums, 4)

print(np.dot(result, np.eye(3, 3)))
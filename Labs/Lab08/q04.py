import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]   # where S15 is actually string data type
details = [('Ali', 10, 38.5), ('Fasih', 12, 53.5),('Owais', 15, 42.10), ('Abser', 10, 40.11)]
# create a structured array
arr = np.array(details, dtype=data_type)

print("Original array:")
print(arr)
print("Sort by height")
print(np.sort(arr, order='height'))
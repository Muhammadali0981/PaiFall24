import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('Iris.csv')

# Task 1
sepal_length = df['SepalLengthCm']
petal_length = df['PetalLengthCm']

plt.figure(figsize=(10, 6))
plt.plot(sepal_length, petal_length, marker='o', linestyle='-', color='b', markersize=5)
plt.title('Petal Length vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid()
plt.show()

 
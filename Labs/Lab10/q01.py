import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ENB2012_data.csv")
plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X1",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X2",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X3",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X4",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X5",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X6",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X7",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="X8",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="Y1",legend=True)
plt.show()

plt.figure(figsize=(4, 2))
sns.boxplot(data = df, x="Y2",legend=True)
plt.show() 
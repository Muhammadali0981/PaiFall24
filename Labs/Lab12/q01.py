import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv(r'C:\me\PaiFall24\Labs\Lab12\Iris.csv')

scalar = StandardScaler()
df_scaled = scalar.fit_transform(df.copy(deep=True).iloc[:, :-1])

pd.DataFrame(df_scaled).describe()

SSE = []

for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++')
    kmeans.fit(df_scaled)
    SSE.append(kmeans.inertia_)

frame = pd.DataFrame({'Clusters': range(1, 20), 'SSE': SSE})
plt.plot(frame['Clusters'], frame['SSE'])
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++')
kmeans.fit(df_scaled)

predict = kmeans.predict(df_scaled)
frame = pd.DataFrame(df_scaled)

frame['cluster'] = predict
print(frame['cluster'].value_counts())
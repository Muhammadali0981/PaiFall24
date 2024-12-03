import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv(r'C:\me\PaiFall24\Labs\Lab11\heart.csv')


X = df.drop('target',axis = 1)

Y = df['target']

t_size = 0.20
seed = 7

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)
sc = StandardScaler()

X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test)  

result = []

for i in range (1, 251):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    prediction = knn.predict(X_test)
    accuracy = accuracy_score(Y_test, prediction)
    result.append([i, accuracy])
    print(f"k = {i}, Accuracy: {accuracy_score(Y_test, prediction):.4f}")

result = pd.DataFrame(result, None ,['K', 'Accuracy']);
max = result.loc[result['Accuracy'].idxmax()]
min = result.loc[result['Accuracy'].idxmin()]
print(f"Best K: {max['K']}, Max Accuracy: {max['Accuracy']:}")
print(f"Worst K: {min['K']}, Max Accuracy: {min['Accuracy']:}");
sns.regplot(x=result['K'],y = result["Accuracy"], line_kws={'color':'red'}, scatter_kws={'color':'darkblue', 'alpha':0.2, 'edgecolor':'black'})
plt.show()
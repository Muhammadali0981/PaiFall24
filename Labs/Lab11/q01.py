import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('heart.csv')


X = df.drop('target',axis = 1)

Y = df['target']

t_size = 0.20
seed = 7

X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

for i in range (1, 251):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_test)
    print(accuracy_score(Y_test, predictions))

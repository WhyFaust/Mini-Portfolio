import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
#получаем данные
df = pd.read_csv("./weatherData.csv")
#данные о таблице
df.shape
df.info()
# Precip Type (тип осадков) встречается только в виде дождя и снега
df['Precip Type'].value_counts()
# Summary бывают различных типов. Чаще всего - `Partly Cloudy`
df['Summary'].value_counts()
# Сначала разделим на признаки (X), и ответы (y)
# предсказывать будем Summary, сам прогноз погоды
y = df['Summary']
X = df.drop(['date', 'Summary', 'Precip Type'], axis=1)
# Теперь можно поделить на тестовую и валидационную выборку в соотношении 0.3
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)


gauss = GaussianNB()
gauss.fit(X_train, y_train)
y_pred = gauss.predict(X_test)
accuracy_score(y_test, y_pred)


des_tree = DecisionTreeClassifier()
des_tree.fit(X_train, y_train)
y_pred = des_tree.predict(X_test)
accuracy_score(y_test, y_pred)


sgd = SGDClassifier(n_jobs=-1)
sgd.fit(X_train, y_train)
y_pred = sgd.predict(X_test)
accuracy_score(y_test, y_pred)

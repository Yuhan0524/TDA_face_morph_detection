from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def RFC(data):
    iris = data
    for i in range(20):
        accuracy = []
        for i in range(20):
            x_train, x_test, y_train, y_test = train_test_split(data, label, random_state=6)
            transfer = StandardScaler()
            x_train = transfer.fit_transform(x_train)
            x_test = transfer.transform(x_test)
            estimator = KNeighborsClassifier()
            estimator.fit(x_train, y_train)
            y_predict = estimator.predict(x_test)
            # print(estimator.score(x_test, y_test))
            accuracy.append(estimator.score(x_test, y_test))
        print(sum(accuracy) / 20)


morph = [[14, 10, 8, 12, 11, 12, 15, 17],[17, 14, 7, 8, 7, 15, 9, 9],[6, 7, 10, 11, 13, 19, 18, 7],[23, 17, 13, 14, 13, 13, 19, 18],[15, 15, 12, 15, 17, 18, 14, 18],[27, 8, 8, 15, 17, 18, 25, 17],[11, 10, 8, 7, 15, 9, 22, 14],[16, 15, 12, 10, 3, 16, 19, 17],[20, 11, 5, 10, 10, 13, 18, 11],[20, 8, 7, 10, 10, 7, 20, 11]]
origin = [[17, 18, 16, 11, 10, 19, 31, 21],[16, 13, 13, 18, 23, 13, 22, 18],[17, 14, 13, 16, 16, 21, 17, 24],[15, 19, 13, 21, 16, 20, 23, 31],[16, 15, 23, 26, 18, 20, 20, 17],[19, 19, 17, 27, 18, 25, 28, 35],[24, 24, 16, 22, 16, 31, 29, 23],[10, 9, 8, 15, 10, 19, 31, 13],[18, 15, 15, 9, 10, 18, 23, 21],[15, 18, 9, 11, 14, 17, 24, 26]]
label = [0]*10 + [1]*10
data = origin+morph
RFC(data)
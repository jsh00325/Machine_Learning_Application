import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets


diabetes = datasets.load_diabetes()
diabetes_X, diabetes_Y = datasets.load_diabetes(return_X_y=True)

# 데이터 속성 명
print(diabetes.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

diabetes_X_new = diabetes_X[:, 2][:, np.newaxis]
print(diabetes_X_new.shape)

# 테스트 데이터(10%)와 학습 데이터(90%) 분리
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(diabetes_X_new, diabetes_Y, test_size=0.1, random_state=0)

regr = LinearRegression()
regr.fit(X_train, y_train)

plt.scatter(X_test, y_test, color="black")

y_pred = regr.predict(X_test)
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.show()
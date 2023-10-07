import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0], [1], [2]]
y = [3, 3.5, 5.5]

reg.fit(X, y)

# 기울기
print(reg.coef_)

# 절편
print(reg.intercept_)

# 얼마나 잘 맞는지 점수
print(reg.score(X, y))

plt.scatter(X, y, color="black")

# 예측값으로 선 그래프 그리기
y_pred = reg.predict(X)
plt.plot(X, y_pred, color="blue")

plt.show()
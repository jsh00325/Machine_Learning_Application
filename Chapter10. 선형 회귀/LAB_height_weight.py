import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

X = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]

reg.fit(X, y)

print(f'키 {165}cm의 몸무게는 {reg.predict([[165]])[0]:.2f}kg으로 예측됨.')

y_pred = reg.predict(X)

plt.scatter(X, y, color="black")
plt.plot(X, y_pred, color="red")
plt.show()
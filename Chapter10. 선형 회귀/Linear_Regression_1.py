import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.0, 1.0, 2.0])
Y = np.array([3.0, 3.5, 5.5])

w, b = 0, 0
lrate = 0.01	# 학습률
epochs = 1000	# 반복 횟수

n = float(len(X))

for i in range(epochs) :
	y_pred = w * X + b	# 선형 회귀 예측 값

	dw = (2 / n) * sum(X * (y_pred - Y))
	db = (2 / n) * sum(y_pred - Y)

	w = w - lrate * dw	# 기울기 수정
	b = b - lrate * db	# 절편 수정

print(f'f(x) = {w}x + {b}')
y_pred = w * X + b

plt.scatter(X, Y)
plt.plot([X[0], X[-1]], [y_pred[0], y_pred[-1]], color='red')

plt.show()
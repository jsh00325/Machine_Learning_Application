from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x_idx, y_idx = 0, 1

def show_graph() :
	formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

	plt.figure(figsize=(5, 4))
	plt.scatter(iris.data[:, x_idx], iris.data[:, y_idx], c=iris.target)
	plt.colorbar(ticks=[0,1,2], format=formatter)

	plt.xlabel(iris.feature_names[x_idx])
	plt.ylabel(iris.feature_names[y_idx])

	plt.tight_layout()
	plt.show()

X = iris.data
Y = iris.target

knn = KNeighborsClassifier(n_neighbors=5)

"""
# 학습 80 : 20 테스트
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)

knn.fit(X_train, Y_train)

Y_pred = knn.predict(X_test)
score = metrics.accuracy_score(Y_test, Y_pred)
"""

# 모든 데이터에 대해서 학습
knn.fit(X, Y)

X_new = [[3,4,5,2], [5,4,2,2]]
Y_new_pred = knn.predict(X_new)

print(X_new[0], "-", iris.target_names[Y_new_pred[0]])
print(X_new[1], "-", iris.target_names[Y_new_pred[1]])
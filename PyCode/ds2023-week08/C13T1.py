from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans  

iris = load_iris()
type(iris)
print (iris.feature_names)
print (iris.target_names)

# store features matrix in "X"
X = iris.data
# store response vector in "y"
Y = iris.target

def Model(n_clusters):
    estimator = KMeans(n_clusters=n_clusters)# 构造聚类器
    return estimator

def train(estimator):
    estimator.fit(X)  # 聚类
# 初始化实例，并开启训练拟合
estimator=Model(3)     
train(estimator)     
label_pred = estimator.labels_  # 获取聚类标签
# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show() 
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression  # 多元线性回归算法
# 生成训练数据和测试数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
train = data
# boston = datasets.load_boston()
# train = boston.data  # 样本
# target = boston.target  # 标签

# 切割数据样本集合测试集
X_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.2)  # 20%测试集；80%训练集

# 创建学习模型
linear = LinearRegression()


linear.fit(X_train, y_train)
print(linear.coef_)
y_pre_linear = linear.predict(x_test)
re1=linear_score = r2_score(y_train, linear.predict(X_train))
print('train:',re1)
re2=linear_score = r2_score(y_test, y_pre_linear)
print('test:',re2)

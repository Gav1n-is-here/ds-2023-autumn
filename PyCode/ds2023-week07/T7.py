#梯度下降法
import pandas as pd
from numpy import dot
from sklearn import datasets
import numpy as np
from matplotlib import pyplot as plt
# w未知参数
from sklearn.preprocessing import StandardScaler
 
plt.rcParams['font.sans-serif'] = ['SimHei']
 
def logit(x):
 
  return 1./(1+np.exp(-x))
 
def loss_function(w,x,y):
    r_y = dot(y.T,logit(x.dot(w)))+dot((1-y).T,logit(1-x.dot(w)))
    return r_y.T
 
 
def get_grad(w,x,y):
 
    grad = (logit(x.dot(w))-y).T.dot(x)
    return grad.T
 
 
def gradient_function(w0,x,y,theata):
    k = 0
    grad = get_grad(w0,x,y)
    list=[]
    w1 = np.random.random((x.shape[1],1))
 
    while k<1000:
            w0 = w1
            grad = get_grad(w0,x,y)
            w1 = w0 - theata * grad
            list.append(loss_function(w1,x,y)[0])
            k+=1
    return w1,loss_function(w1,x,y),k,list
 
 

iris=datasets.load_iris()
#每行的数据，一共四列，每一列映射为feature_names中对应的值
X=iris.data
#每行数据对应的分类结果值（也就是每行数据的label值）,取值为[0,1,2]
Y = iris.target

from sklearn.utils import shuffle
X,Y = shuffle(X,Y, random_state=1337)#打乱
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)  # 20%测试集；80%训练集

x_train = x_train[np.where(y_train<2),:].reshape(-1,4)
y_train= y_train[np.where(y_train<2)].reshape(-1,1)
x_test=x_test[np.where(y_test<2),:].reshape(-1,4)
y_test=y_test[np.where(y_test<2)].reshape(-1,1)
#归一化处理
x = StandardScaler().fit_transform(x_train)
x_test = StandardScaler().fit_transform(x_test)
x = np.hstack((x, np.ones((x.shape[0], 1))))
x_test= np.hstack((x_test, np.ones((x_test.shape[0], 1))))
theata=0.0001
 
w0 = np.random.random((x.shape[1],1))
 
 
w,loss,k,list=gradient_function(w0, x, y_train, theata)

print("参数",w)
print("损失函数值：",loss)
print("迭代次数：",k)
 
 
r_y = logit(dot(x, w))

r_y_test=logit(dot(x_test, w))
from sklearn.metrics import r2_score
re1= r2_score(y_train, r_y)
print('train:',re1)
re2 = r2_score(y_test, r_y_test)
print('test:',re2)

 
plt.subplot(2,1,1)
plt.plot(y_train, color="red", marker="o", label="实际")
plt.plot(r_y, color="blue", marker=".", label="预测")
plt.xlabel("Sample", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.subplot(2,1,2)
plt.plot(list, color="blue", marker=".", label="损失值")
plt.legend()
plt.show()
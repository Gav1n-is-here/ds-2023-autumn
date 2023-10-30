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

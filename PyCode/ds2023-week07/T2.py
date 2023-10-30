import numpy
from numpy import random
x=numpy.random.uniform(0,10,30)
# y=9*x+8
# print(x,y)
# y+=numpy.random.normal(0,1,1)
# print(x,y)
for i in x:
    y=9*i+8+numpy.random.normal(0,1,1)
    print('x=',i,'y=',y,'\n')

import random
import math
num_all = 0         #随机点总计数器
num_in = 0         #随机点在内的计数器
num_halt = 10000000 

for i in range(num_halt): 
    x = random.random()         #获得随机点的横坐标
    y = random.random()*25         #获得随机点的纵坐标
    if y< x*x+4*x*math.sin(x) :          #随机点(x,y)在内
        num_in = num_in + 1   #内计数器+1
    num_all = num_all + 1      
    re = 25*num_in/num_all
print('round:',num_all,'result=', re)

import pandas as pd
from functools import reduce
import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_excel("gpu_data.xlsx")
df=pd.DataFrame(df)
date=df.columns.values[4:]
# print(date)

dfsort = df.sort_values(by="performance",ascending=True) 

for k in date:
    per=dfsort.loc[:,k].values

    rows=dfsort.shape[0]
    # print(rows)
    x=dfsort.loc[:,'performance'].values
    y=per
    data = []

    import random

    for i in range (0,rows):
        if (1):
            for j in range(0,int(y[i]*100)):
                r=random.uniform(-10, 10)

                data.append(x[i]+r)
                # print(r)
    # print(x)
    # print(len(data))

    import matplotlib.pyplot as plt
 
    plt.hist(data,bins=50)
 
    plt.title(k)

    plt.show()
    

# from scipy import stats

# # print (data)
# # 拟合分布
# from fitter import Fitter
# f = Fitter(data,timeout=200)  # 创建Fitter类
# f.fit()  # 调用fit函数拟合分布
# f.summary()  # 输出拟合结果


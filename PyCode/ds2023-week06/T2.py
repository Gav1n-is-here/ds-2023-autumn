import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

re =  np.random.normal(0,1,100)
x = np.arange(-5, 5, 0.1)
segments=pd.cut(re,x,right=False)
print(segments)
counts=pd.value_counts(segments,sort=False)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决pythonmatplotlib绘图无法显示中文的问题
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.subplot(111)
plt.plot(counts.index.astype(str),counts, 'b-', linewidth=2)
plt.show()
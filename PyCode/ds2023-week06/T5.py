import numpy as np

x = np.array([1.0,-1.0,4.0])
y = np.array([2.0,1.0,3.0])
z=np.array([1.0,3.0,-1.0])
# 归一化数据
scaled_x = x-np.mean(x)
scaled_y = y-np.mean(y)
scaled_z = z-np.mean(z)
# 组成矩阵
data = np.matrix([[scaled_x[i], scaled_y[i],scaled_z[i]] for i in range(len(scaled_x))])

# 求协方差矩阵
cov_matrix= np.dot(data.T, data)/(len(x)-1)
print(cov_matrix)
import numpy as np

mat = np.array([[2,1],
              [4,5],])

eigenvalue, featurevector = np.linalg.eig(mat)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)
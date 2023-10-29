import numpy as np

x = np.array([1.0,-1.0,4.0])
y = np.array([2.0,1.0,3.0])
z=np.array([1.0,3.0,-1.0])

scaled_x = x-np.mean(x)
scaled_y = y-np.mean(y)
scaled_z = z-np.mean(z)

data = np.matrix([[scaled_x[i], scaled_y[i],scaled_z[i]] for i in range(len(scaled_x))])

cov_matrix= np.dot(data.T, data)/(len(x)-1)

def eig_power(A,v0,eps):
    uk = v0
    flag = 1
    val_old = 0
    n = 0
    while flag:
        n = n+1
        vk = A*uk        
        val = vk[np.argmax(np.abs(vk))]        
        uk = vk/val              
        if (np.abs(val-val_old)<eps):
            flag = 0
        val_old = val
        
    print('max eigenvalue:',val)
    print('eigenvector:',np.asarray(uk).flatten())
    print('iteration:',n)
    return val, uk  
    
if __name__ == '__main__':
    v0 = np.matrix([[1],[1],[1]], dtype='float')
    eps = 1
    val,uk = eig_power(cov_matrix,v0,eps)
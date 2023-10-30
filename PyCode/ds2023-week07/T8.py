from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
import math
iris = load_iris()
type(iris)
# print (iris.feature_names)
# print (iris.target_names)

# store features matrix in "X"
X = iris.data
# store response vector in "y"
Y = iris.target

setosa_count=0
versicolor_count=0
virginica_count=0
setosa=[0,0,0,0]
versicolor=[0,0,0,0]
virginica=[0,0,0,0]
for i in range (len(Y)):
    if(Y[i]==0):
        setosa_count+=1
        setosa+=X[i]
        # print(i,X[i])
        # print(setosa)
    elif(Y[i]==1):
        versicolor_count+=1
        versicolor+=X[i]
    elif(Y[i]==2):
        virginica_count+=1
        virginica+=X[i]

# print(setosa)
# print(setosa_count)
print('mean of setosa:',setosa/setosa_count)
print('mean of versicolor:',versicolor/versicolor_count)
print('mean of virginica:',virginica/virginica_count)

def compute_distence(i):
    if(0<=i):
        if(Y[i]==0):
            mean=setosa/setosa_count
            return math.sqrt((X[i,0]-mean[0])**2+(X[i,1]-mean[1])**2+(X[i,2]-mean[2])**2+(X[i,3]-mean[3])**2)
        elif(Y[i]==1):
            mean=versicolor/versicolor_count
            return math.sqrt((X[i,0]-mean[0])**2+(X[i,1]-mean[1])**2+(X[i,2]-mean[2])**2+(X[i,3]-mean[3])**2)
        elif(Y[i]==2):
            mean=versicolor/versicolor_count
            return math.sqrt((X[i,0]-mean[0])**2+(X[i,1]-mean[1])**2+(X[i,2]-mean[2])**2+(X[i,3]-mean[3])**2)
    else:
        return -1
for i in range (len(Y)):
    print(i,'distance:',compute_distence(i))

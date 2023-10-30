from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
iris = load_iris()
type(iris)
print (iris.feature_names)
print (iris.target_names)

# store features matrix in "X"
X = iris.data
# store response vector in "y"
Y = iris.target
print (X[0:1],Y[0:1])
from sklearn.utils import shuffle
X,Y = shuffle(X,Y, random_state=1337)#打乱
print (X[0:1],Y[0:1])

print("X=",X)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)  # 20%测试集；80%训练集
print('x_test=',x_test)
print('x_train=',x_train)
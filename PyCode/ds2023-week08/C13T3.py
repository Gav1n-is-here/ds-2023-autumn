from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
iris = load_iris()
type(iris)
# store features matrix in "X"
X = iris.data
# store response vector in "y"
Y = iris.target
from sklearn.utils import shuffle
X,Y = shuffle(X,Y, random_state=1337)
print("X=",X)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)  # 20%测试集；80%训练集
print('x_test=',x_test)
print('x_train=',x_train)
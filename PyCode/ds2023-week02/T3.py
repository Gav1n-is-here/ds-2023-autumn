import numpy as np
#每个node内向量的顺序：人，狼，羊，菜，1表示在初始岸，0表示在对岸
nodegraph=np.array([[1,1,1,1],[1,1,1,0],[1,1,0,1],[1,0,1,1],[1,0,1,0],[0,1,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
mov=np.array([[1,0,0,0],[1,1,0,0],[1,0,1,0],[1,0,0,1]])
graph=np.zeros((10, 10), dtype=int)
re=np.array([0])
for i in range(0,10,1):
    for j in range(0,4,1):
        arrtest=np.array([0,0,0,0])
        arrtest=np.bitwise_xor(nodegraph[i,],mov[j,])
        re=np.where((nodegraph == arrtest).all(axis=1))
        if(re[0]in range(10)):
            graph[i,re[0]]=1

stack=[0]*10
def bfs(start,resu):
    stack[start]=1
    resu.append(start)
    if start==9:
        print(resu)
    for i in range(10):
        if graph[start][i]==1 and stack[i]==0:
            bfs(i,resu)
    stack[start]=0
    resu.pop()

bfs(0,[])

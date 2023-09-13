Lin=input('列表:').split(",")
L1=[(Lin[i]) for i in range(len(Lin)-1,-1,-1)]
n=len(Lin)
L2=[]
while (n>0):
    n-=1
    L2.append((Lin[n]))
print('for循环',L1)
print('while循环',L2)
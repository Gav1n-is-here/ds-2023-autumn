from typing import List
def compute(arr:List[int],n):
    muti=1
    for i in range(0,len(arr),1):
        if i+1 !=n:
            muti*=arr[i]
    return muti
n=int(input("please inout n:"))
A = list(range(1,n,1))
B=[]
for i in range(1,n,1):
    B.append(compute(A,i))
print('A:',A)
print('B:',B)


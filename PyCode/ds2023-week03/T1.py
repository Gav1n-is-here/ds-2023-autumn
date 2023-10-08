n=(input('please input a number: '))
inter,fraction=n.split('.')
L=len(fraction)
inter=int(inter)
fraction=int(fraction)
fraction=fraction/10**L
stack1=[0]*100
stack2=[0]*100
i=0
if inter ==1:
    stack1[0]=1
else:    
    while (inter!=0 and inter!=1):
        stack1[i]=inter%2
        inter=inter//2
        i+=1
        stack1[i]=inter
j=0
if fraction==0:
    stack2[0]=0
    j=1
else:
    while fraction!=0:
        stack2[j]=int(fraction*2)
        fraction=fraction*2-stack2[j]
        j+=1
print('the binary of',n,' is :0b',end='')
for k in range(i,-1,-1):
    print(stack1[k],end='')
print('.',end='')
for k in range(0,j):
    print(stack2[k],end='')
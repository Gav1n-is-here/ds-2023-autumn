n=int(input('input a number:'))
print(n,end='')
re=1
while (n!=0):
    re*=n
    n-=1
print('!=',re)
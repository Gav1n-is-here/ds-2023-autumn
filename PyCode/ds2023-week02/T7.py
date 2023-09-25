print('x(n+1)=x(n)-[x(n)^3-c]/[3*x(n)^2]')
c=10
g=c/2
i=0
while abs(c-g**3)>0.00000000001:
    g=g*2/3+c/3/g**2
    i+=1
    print('%d:g=%.13f'%(i,g))
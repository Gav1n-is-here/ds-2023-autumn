c=2
g=c/4
i=0
print('g=c/4:')
while abs(c-g*g)>0.00000000001:
    g=(g+c/g)/2
    i+=1
    print('%d:g=%.13f'%(i,g))

g=c/2
i=0
print('g=c/2:')
while abs(c-g*g)>0.00000000001:
    g=(g+c/g)/2
    i+=1
    print('%d:g=%.13f'%(i,g))

g=c/1
i=0
print('g=c:')
while abs(c-g*g)>0.00000000001:
    g=(g+c/g)/2
    i+=1
    print('%d:g=%.13f'%(i,g))
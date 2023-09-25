c=int(input('input a number:'))
g=c/2
i=0
while abs(c-g*g)>0.00000000001:
    g=(g+c/g)/2
    i+=1
    print('%d:g=%.13f'%(i,g))
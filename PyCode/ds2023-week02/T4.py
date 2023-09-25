c=2
r=0
g=0
for i in range(0,c+1):
    if i*i>c:
        g=i-1
        break
while (c-g*g)>=0.0001:
    g+=0.00001
    r+=1
    print('round','%d:g=%.5f'%(r,g))

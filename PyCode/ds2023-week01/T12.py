y=float(input('input a number:'))

l = -1e4
r = 1e4
while(r - l > 1e-8):
    mid = (l + r) / 2
    
    if(mid * mid * mid >= y):
        r = mid
    else:   
        l = mid
print (l)   

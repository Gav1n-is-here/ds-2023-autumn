#Machin
n=10
t = n+10                                     #多计算10位，防止尾数取舍的影响
b = 10**t                                    #为算到小数点后t位，两边乘以10^t
x1 = b*4//5                                  #取整求含4/5的首项
x2 = b // -239                               #取整求含1/239的首项
s = x1+x2                                    #求第一大项
n *= 2                                       #设置下面循环的终点，即共计算n项
for i in range(3, n, 2):                     #循环初值=3，末值n,步长=2
    x1 //= -25                               #取整求每个含1/5的项及符号
    x2 //= -57121                            #取整求每个含1/239的项及符号
    x = (x1+x2) // i                         #求两项之和，除以对应因子，取整
    s += x                                   #求总和
pai = s*4                                    #求出π
pai //= 10**10                               #舍掉后十位
print(pai/10000000000,'round:',i)           

#
pai=pai/10000000000
i=0
pi=0
while True :
    pi=pi+3*(1/(4*i+1)/(2*i+1)/(i+1))
    i+=1
    piy=float(format(pi,'.10f'))
    if(piy==pai):
        break
print(piy,'round',i)

#
i=0
pi=0
while True :
    pi=pi+(1/16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    i+=1
    piy=int(pi*10000000000)/10000000000
    if(piy==pai):
        break
print(piy,'round',i)
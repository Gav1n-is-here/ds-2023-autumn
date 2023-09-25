# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


out= 1
twoc=0
threec=0
n =int(input("n="))
def T1(ni): 
    global out
    global twoc
    global threec
    if((ni!=3)&(ni!=2)):

        pa=ni//2
        pb=ni-ni//2
        T1(pa)
        T1(pb)
    else:
        
        out =out*ni
        if(ni==2):
            twoc+=1
        elif(ni==3):
            threec+=1
        else:
            print('erro')
    return

T1(n)
print("when n =",n,', it`s ',out,'= 2^',twoc,'x 3^',threec)

# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
w =input("w=")
x =input("x=")
y =input("y=")
z =input("z=")

listxyz =[w,x,y,z]
n1=max(listxyz)
listxyz.pop(listxyz.index(n1))
n2=max(listxyz)
listxyz.pop(listxyz.index(n2))
n4=min(listxyz)
listxyz.pop(listxyz.index(n4))
n3=min(listxyz)
print(n1,n2,n3,n4)
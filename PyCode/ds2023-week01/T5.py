# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

x =(input("x="))
y =(input("y="))
z =(input("z="))
listxyz =[x,y,z]
minn=min(listxyz)
maxn=max(listxyz)
print(listxyz.index(minn))
listxyz.pop(listxyz.index(minn))
midn=min(listxyz)
print(minn,midn,maxn)

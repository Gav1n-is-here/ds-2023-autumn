str1=input('input a string:')
List1=[]
flag=0
for i in str1:
    List1.append(i)
for i in range(1,len(List1)-1):
    if(List1[i]==List1[i+1]):
        i+=1
        flag=1
print('Y'if flag==1 else 'N')

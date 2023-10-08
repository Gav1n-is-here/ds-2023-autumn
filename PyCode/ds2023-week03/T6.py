score=int(input("please input your score:"))
if(score<0 or score>100):
    print("invalid score")
if score<=60:
    print("your grade is D")
elif score<=74:
    print("your grade is C")
elif score<=89:
    print("your grade is B")
elif score>=90:
    print("your grade is A")
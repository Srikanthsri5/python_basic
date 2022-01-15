num=int(input("enter a number"))
n1=num
rev=0
while(n1>0):
    q=n1//10
    r=n1%10
    rev=r+10*rev
    n1=q
print("number:",num)
print("reverse: ",rev)


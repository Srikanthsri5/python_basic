num=int(input("enter a number: "))
n1=num
sum=0
i=0
while n1>0:
    r=n1%10
    if(r==9):
        r=0
    else:
        r=r+1
    q=n1//10
    sum=sum+r*pow(10,i)
    i=i+1
    n1=q
print(sum)

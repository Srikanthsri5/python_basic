num=int(input("enter a number: "))
sum=0
temp=num
while temp>0:
    dig=temp%10
    sum+=dig**3
    temp//=10
if num==sum:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")
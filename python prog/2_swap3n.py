print("enter three integers")
a=int(input())
b=int(input())
c=int(input())
print("values before swapping")
print("A:",a,"B:",b,"C:",c)
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print("values after swapping")
print("A:",a,"B:",b,"C:",c)
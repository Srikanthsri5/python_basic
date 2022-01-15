'''
n=int(input("enter a number"))
n1=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(n1==rev):
    print("palindrome")
else:
    print("not palindrome")
'''   
''' 
n=int(input("enter a number "))
sum=0
while(n>0):
    sum=sum+n
    n=n-1
print(sum)
'''
'''
n=int(input("enter a number "))
n1=n
sum=0
while n1!=0:
    r=n1%10
    sqr=r*r
    sum=sum+sqr
    q=n1//10
    n1=q
print(sum)
'''
'''
n=int(input("enter a number "))
n1=n
sum=0
while(n1>0):
    r=n1%10
    sum=sum+r**3
    n1=n1//10
if(n==sum):
    print("arm")
else:
    print("not arm")
'''
'''
ntr=int(input("enter range"))
n1,n2=0,1
count=0
if(ntr<=0):
    print("enter an integer!")
elif(ntr==0):
    print(n1)
else:
    print("fibonacci ")
    while(count<ntr):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
'''
'''
dn=int(input("enter decimal number :"))
bn=0
i=1
while dn>0:
    rem=dn%2
    dn=dn//2
    bn=bn+(rem*i)
    i=i*10
print(bn)
'''
'''
bn=int(input("enter a binary number: "))
dn=0
i=1
while bn!=0:
    rem=bn%10
    dn=dn+(rem*i)
    i=i*2
    bn=bn//10
print(dn)
'''

n=int(input("enter a number"))
n1=n
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
n=int(input("enter a number:\n"))
n1=n
sum=0
while n1>0:
	q=n1//10
	r=n1%10
	sum=sum+r
	n1=q
print("num:",n)
print("sum of the digits:",sum)
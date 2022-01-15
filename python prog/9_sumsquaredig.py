n=int(input("enter integer number"))
n1=n
sum=0
while n1!=0:
	r=n1%10
	sqr=r*r
	sum=sum+sqr
	q=n1//10
	n1=q
print("sum of square of digit is:\n")
print(sum)
d=int(input("enter a number:\n"))
sum=0
i=1
while d>0:
	rem=d%2
	d=d//2
	sum=sum+rem*i
	i=i*10
print(sum)

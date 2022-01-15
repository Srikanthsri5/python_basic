bnum=int(input("enter a bin ary no:"))
dnum=0
i=1
while bnum!=0:
	rem=bnum%10
	dnum=dnum+(rem*i)
	i=i*2
	bnum=bnum//10
print("decimal number is:\n")
print(dnum)
    
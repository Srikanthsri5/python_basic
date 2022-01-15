nterms=int(input("enter range: "))
n1,n2=0,1
count=0
if nterms<=0:
    print("enter positive number:")
elif nterms==1:
    print("fibo upto",nterms)
    print(n1)
else:
    print("fibo squence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
    
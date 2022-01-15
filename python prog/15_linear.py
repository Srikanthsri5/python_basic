a=[92,71,65,23,10,76,12]
key=int(input("enter element to be searched: "))
flag=0
for i in range(len(a)):
    if(key==a[i]):
        flag=1
        break
if(flag==1):
    print(f'{key} found in list')
else:
    print(f'{key} not found in list')
    
a=[12,6,8,5,9,13,17]
ek=ok=0
esum=osum=0
for i in range(len(a)):
    if(a[i]%2==0):
        ek=ek+1
        esum=esum+a[i]
    else:
        ok=ok+1
        osum=osum+a[i]
print("number of even integers: ",ek)
print("sum of even numbers: ",esum)
print("number of odd integers: ",ok)
print("sum of odd numbers: ",osum)
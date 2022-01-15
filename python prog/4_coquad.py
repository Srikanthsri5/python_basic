print("enter x and y values")
x=int(input())
y=int(input())
if(x>0 and y>0):
    print(f'{x} and {y} values are in first quadrand')
elif(x<0 and y>0):
    print(f'{x} and {y} values are in second quadrand')
elif(x<0 and y<0):
    print(f'{x} and {y} values are in third quadrand')
else:
    print(f'{x} and {y} values are in fourth quadrand')


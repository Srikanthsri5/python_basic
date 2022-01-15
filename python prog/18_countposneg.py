"""
a=[12,3,-15,0,-45,0,0,5,9,13,17]
pc=zc=nc=0
for i in range(len(a)):
    if(a[i]>0):
        pc=pc+1
    elif(a[i]==0):
        zc=zc+1
    else:
        nc=nc+1
print("number of positive integers: ",pc)
print("number of negative integers: ",nc)
print("number of zeros: ",zc)
"""
"""

for i in range(18):
    print("virat kohli\n")
    """
"""
#password generator    
import string as s
from random import *
ch = s.ascii_letters+s.digits+s.punctuation
password="".join(choice(ch) for x in range(randint(8,16)))
print(password)
"""

#insta logo
from turtle import*

bgcolor('black')
pencolor('red')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(34,90)
    
penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)
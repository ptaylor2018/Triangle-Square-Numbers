'''
Created on Jul 17, 2016

@author: Patrick
'''
from math import sqrt
def leap_frog(start_val):
    restart_val= sqrt(start_val)
    bottom_range= int(round(restart_val*5.82))
    top_range=int(round(restart_val*5.84))
    for i in range(bottom_range,top_range+1):
        poss_tri= i**2
        test = poss_tri*8 +1
        if sqrt(test).is_integer():
            return poss_tri
    
p=0
initial_num= 1
num= initial_num
numbers=[]
square_places=[]
triangle_places=[]
# print leap_frog(36)
for i in range(0,10):
    frogged=leap_frog(num)
    print frogged
    numbers.append(frogged)
    square_places.append(int(sqrt(frogged)))
    triangle_place= ((sqrt(frogged*8 +1)-1)/2)
    triangle_places.append(int(triangle_place))
    num=frogged
print "Triangle-Square Numbers"
print numbers
print "Square Places"
print square_places
print"Triangle Places"
print triangle_places

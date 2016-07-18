'''
Created on Jul 17, 2016

@author: Patrick
'''
from numpy import sqrt
num_range = 10000
square_numbers = [i**2 for i in range(1,num_range)]
triangle_numbers=[((i*(i+1))/2) for i in range(1,num_range)]
square_place=[]
triangle_place=[]
triangle_square_numbers=[]
for n in square_numbers:
    if n in triangle_numbers:
        triangle_square_numbers.append(n)
        triangle_place.append(triangle_numbers.index(n) +1)
        square_place.append(square_numbers.index(n) +1)
print "Triangle-Square Numbers:"
print triangle_square_numbers
print "Triangle Places:"
print triangle_place
print "Square Places:"
print square_place

    
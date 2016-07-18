'''
Created on Jul 17, 2016

@author: Patrick Taylor (with the assistance of Kate Minker)
'''


import decimal
from decimal import *
from math import sqrt
number_wanted= int(raw_input("How many triangle square numbers do you desire?(Can handle up to and including 200)"))
import time # some stuff to see how long the operation takes
start_time=time.time()

def leap_frog(start_val):
    restart_val= sqrt(start_val) # this takes the starting value in the list of triangle squares and gives its square root counter part, which is used to determine bottom_range
    bottom_range= int(round(restart_val*(5.82842712474619)))
    while(True):
        poss_tri= bottom_range**2 #this makes the bottom_range a square number, fulfilling criterion 1
        test = poss_tri*8 +1 # this(with the next line) checks if poss_tri is in fact a triangle number. if test is a perfect square, it is!
        if (sqrt(Decimal(test)))% 1 ==0: # so I wanted to make this an integer sqrt test so I could go above 200, but isqrt is way slower than sqrt.
            return poss_tri
        else:
            bottom_range+=1 # if the value tested isn't correct, it adds one and tries again.

initial_num= 1 
num= initial_num
numbers=[1]
square_places=[1]
triangle_places=[1]

for i in range(0,number_wanted):
    
    frogged=leap_frog(num)
    print frogged
    numbers.append(frogged)
    square_places.append(int(sqrt(frogged)))
    triangle_place= (int(sqrt(frogged*8 +1)-1)/2)
    triangle_places.append(int(triangle_place))
    num=frogged
    
    
    
#printout    
print "Triangle-Square Numbers"
print numbers
print "Square Places"
print square_places
print"Triangle Places"
print triangle_places
#This next block was used to determine what the approached value for bottom_range was
'''quotients = [((square_places[i+1]*1.0)/(square_places[i]*1.0)) for i in range(len(square_places)-1)] 
print "square places quotients"
print quotients
diffs = [quotients[i]-quotients[i+1] for i in range(len(quotients)-1)]
print "differences of quotients"
print diffs
'''
print(" This took %s seconds to do" %(time.time()-start_time))

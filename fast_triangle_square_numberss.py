'''
Created on Jul 17, 2016

@author: Patrick
'''
#import sys
from math import sqrt
import gmpy2
from gmpy2 import isqrt
import time
start_time=time.time()
def leap_frog(start_val, top_fact):
    restart_val= sqrt(start_val)
    bottom_range= long(round(restart_val*(5.82842712474619)))
    top_range_set= long(round(restart_val*top_fact))
    top_range= top_range_set -((top_range_set - bottom_range)/2)
    #for i in range(bottom_range,top_range+1):
    while(True):
        poss_tri= bottom_range**2
        test = poss_tri*8 +1
        if (sqrt(test)).is_integer():
            return poss_tri
        else:
            bottom_range+=1
p=0
initial_num= 1225
num= initial_num
numbers=[36,1225]
square_places=[6,35]
triangle_places=[8,49]
# print leap_frog(36)
for i in range(0,100):
    ul_num=numbers[len(numbers)-1]
    penult_num= numbers[len(numbers)-2]
    quot= (sqrt(ul_num)*1.0)/(sqrt(penult_num)*1.0)
    #print quot
    frogged=leap_frog(num, quot)
    print frogged
    numbers.append(frogged)
    square_places.append((sqrt(frogged)))
    triangle_place= (long(sqrt(frogged*8 +1)-1)/2)
    triangle_places.append(long(triangle_place))
    num=frogged
    
    
    
#printout    
print "Triangle-Square Numbers"
print numbers
print "Square Places"
print square_places
print"Triangle Places"
print triangle_places
quotients = [((square_places[i+1]*1.0)/(square_places[i]*1.0)) for i in range(len(square_places)-1)]
print "square places quotients"
print quotients
diffs = [quotients[i]-quotients[i+1] for i in range(len(quotients)-1)]
print "differences of quotients"
print diffs
print(" %s seconds" %(time.time()-start_time))
#print sqrt(2440345580851981401.0)/sqrt(73804512832419600.0)
#print sqrt(2440345580851981401.0*8 +1)
#print sys.maxint
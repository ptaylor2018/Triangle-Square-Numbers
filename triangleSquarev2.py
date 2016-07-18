'''
Created on Jul 17, 2016

@author: Patrick
'''
from __future__ import division
num_range = 10000
output=[]
square_numbers = [i**2 for i in range(1,num_range)]
for i in square_numbers:
    if (i/square_numbers[square_numbers.index(i)-1]) >5.829 and (i/square_numbers[square_numbers.index(i)-1]) <5.84:
        output.append(i)
print output
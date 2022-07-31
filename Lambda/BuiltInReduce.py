#input: some other function, iterables.
#operation: applies funtion to the listy
#output: single value
from functools import reduce

my_list = [1,2,3,4,5,6]
new_list = reduce(lambda a,b:(a*b),my_list)
print(new_list)
#1*2*3*4*5*6
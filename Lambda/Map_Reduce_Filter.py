#Map()
#inputs: function, some iterables
#operation: applies this function to iterables
#output: new list


#list(map(lambda x:x+3,[1,2,3,4]))

def new(a):
    return a*a
x = map(new,[1,2,3,4])
print(x)
print(list(x))



def new(a,b):
    return a*b
x = map(new,[1,2,3,4],[1,2,3,4])
print(x)
print(list(x))


lst = [1,2,3,4,5]
y = list(map(lambda x:x+3,lst))
print(y)

#Reduce()
#input: some other function, iterables.
#operation: applies funtion to the listy
#output: single value
from functools import reduce
#reduce(lambda x:x+3,[1,2,3,4])

#filter()
#inputs: function, some iterables
#operation: applies this function to iterables
#output: new list that satisfies the function

#list(filter(lambda x:x+3,[1,2,3,4]))

def new(i):
    if i>=3:
        return i
j = filter(new,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))
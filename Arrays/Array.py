#array is a DS which can hold more than one value at a time.
# It is a collection or ordered series of elements of the same type.
#homogenious data types only
#import array
#import array as a
#from array import *
'''
import array
a = array.array('I',[1,2,3,4,5]) #array('I', [1, 2, 3, 4, 5])
#name of module, array constyuctor, type code
print(a)
'''
'''
import array as arr
a = arr.array('I',[1,2,3,4,5]) #array('I', [1, 2, 3, 4, 5])
#name of module, array constructor, type code
print(a)
'''
from array import *
a = array('I',[1,2,3,4,5]) #array('I', [1, 2, 3, 4, 5])
#name of module, array constyuctor, type code
print(a)

#accessing with index values
print(a[2])
#add at the end
print(a.append(5))
#count the num
print(a.count(5))
#find the length
print(len(a))
#add element after a[0]
a.insert(1,3)
print(a)
#add multiple numbers at the end
a.extend([1,4342,234,234])
print(a)
print(a)
#reverse
a.reverse()
print(a)
#count of an element
print(a.count(1))
print(a)
#remove last element and return that value
print(a.pop())
print(a)
#remove indexed element and return that value
print(a.pop(0))
print(a)
print(a.pop(-1))
print(a)

#remove element without returning the value
a.remove(1)
print(a)
a.remove(234)
print(a)

#array concatenation
a =array('i',[1,2,3,4])
b =array('i',[5,6,7,8])
c = a+b
print(c)

#slicing array using colon :
print(a[0:3])
print(a[0:-2])
print(a[::-1])

#looping
a = array('i',[1,2,3,4,5])
for x in a:
    print(x)
#slice looop
for x in a[0:-3]:
    print("x",x)

print('while')
b = 0
while b<len(a):
    print(a[b])
    b = b+1
b=0
print("shjgyjgj")
while b<a[2]:
    print(a[b])
    b = b+1



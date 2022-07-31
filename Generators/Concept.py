'''
functions that return traversable objects
produce items one at a time only when required
run along with for loops

'''

# return = yield
# name of method = next()
#produce all items at a time = produce only one item at a time
def new(dict):
    for x,y in dict.items():
        yield x,y
a = {1:'hi',2:"hello"}
b = new(a)
print(b)
print(next(b))
print(next(b))



def myf(i):
    while i>=1:
        yield i
        i+=1
j = myf(2)
print(next(j))
#print(next(j))
#print(next(j))


def ex():
    n = 3
    yield n
    n = n*n
    yield n
v = ex()
print(next(v))
print(next(v))

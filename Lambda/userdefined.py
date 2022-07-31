#user defined functions take lambda as input
def A(x):
    return (lambda y:x+y)
t = A(4)
print(t(8))



#y = y+x
#always add x to the y sent
#y=8, x=4
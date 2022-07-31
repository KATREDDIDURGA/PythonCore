#1. self:
#       extra and mandatory parameter of class methids
# 2. __init__ method:
#        similar to constructors in java
#           runs as soon as object of the class is initiated
#           us ed to do initializations of the object

n = "a,b,,c,d,e"
print(n.split(","))
print(3*1**3)
d_2015 = {'x':10,'y':20}
d_2016 = {'x':100,'z':30,'a':33,'b':66}
print(d_2016.combine_first(d_2015))
print(d_2015)

print(type(3+2.0))

s = 'HeL'
print(s.lower().startswith('hel'))

g1 = 80
g2 = 90
print((g1+g2)/2)

x = 10
print(x%11)
tinytuple = (123,'john')
print(tinytuple*2)

l = [1,2,3,4,5]
l.pop(l = list[-1])

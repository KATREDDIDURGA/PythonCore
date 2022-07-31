#subclass of dictionary
#counting hashable objects
from collections import Counter

a = [1,1,1,2,2,3,4,5,6,6,7]
c = Counter(a)
print(c)
#Counter({1: 3, 2: 2, 6: 2, 3: 1, 4: 1, 5: 1, 7: 1})

#output is a dictionary
print(list(c.elements()))
#[1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7]

print(c.most_common())
#ascending order
#[(1, 3), (2, 2), (6, 2), (3, 1), (4, 1), (5, 1), (7, 1)]

sub = {2:1,6:1}
#remove one 2 and one 6 from the list
print(c.subtract(sub))
print(c.most_common())

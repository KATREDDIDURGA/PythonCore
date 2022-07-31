#remembers the order in which entries were done

from collections import OrderedDict
d= OrderedDict()
d[1] = 'a'
d[2] = 'b'
d[3] = 'c'
d[4] = 'e'
d[5] = 'e'
print(d)
#OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'e'), (5, 'e')])
print(d.keys())
#odict_keys([1, 2, 3, 4, 5])
print(d.items())
#odict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'e'), (5, 'e')])
print(d.values())
#odict_values(['a', 'b', 'c', 'e', 'e'])
d[1] = 'p'
print(d)
#OrderedDict([(1, 'p'), (2, 'b'), (3, 'c'), (4, 'e'), (5, 'e')])
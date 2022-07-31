#create single view of multiple mappings
#similar to dictionary
from collections import ChainMap
a = {
    1:'ed',
     2:'py'
    }
b = {
    3:'ml',
     4:'ai'
    }

a1 = ChainMap(a,b)
print(a1)
#ChainMap({1: 'ed', 2: 'py'}, {3: 'ml', 4: 'ai'})

#calls factory function to supply missing values
from collections import defaultdict
d = defaultdict(int)

d[1] = 'pyth'
d[2] = 'edure'
print(d)
#defaultdict(<class 'int'>, {1: 'pyth', 2: 'edure'})

print(d[3])
#0
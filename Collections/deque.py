#insertion and deletion easily in a list
from collections import deque
a = ['e','d','h','j','fd','th']
d = deque(a)
print(d)#deque(['e', 'd', 'h', 'j', 'fd', 'th'])

d.append('python')
print(d)#deque(['e', 'd', 'h', 'j', 'fd', 'th', 'python'])

d.appendleft('python')
print(d)#deque(['python', 'e', 'd', 'h', 'j', 'fd', 'th', 'python'])

d.pop()
print(d)#deque(['python', 'e', 'd', 'h', 'j', 'fd', 'th'])

d.popleft()
print(d)#deque(['e', 'd', 'h', 'j', 'fd', 'th'])



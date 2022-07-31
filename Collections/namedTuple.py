a = namedtuple('courses','name,technology')
s = a('data science','python')
#courses(name='data science', technology='python')
print(s)

#using list to get a named tuple
a = namedtuple('courses','name,technology')
s = a._make(['artificial intelligence','python'])
print(s)
#courses(name='artificial intelligence', technology='python')

'''_-------------'''
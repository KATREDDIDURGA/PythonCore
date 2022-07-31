#keys can be duplicate
courses = {1:'python',
           2:'ds',
           'third':'ml'}
print(courses)
#fetching
print(courses['third'])
#fetching using method
print(courses.get('third'))
#modifying
courses['third'] = "Hadoop"
print(courses['third'])
#adding key - value to dict
courses['four'] = 'ml'
print(courses['four'])
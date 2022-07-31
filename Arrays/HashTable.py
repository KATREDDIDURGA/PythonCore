#hash table is a type of ds that maps keys to its value pairs
#key is generated using hash function

#step 1: create dictionary. (using {}, ore by using dict()
myDict = {'Dave':'001','Ava':'002','Joe':'003'}
print(myDict)
print(type(myDict))

# newDict = dict()#empty
# print(newDict)
# print(type(newDict))

newDict1 = dict(Dave='001',Ava='002',Joe='003')
print(newDict1)
print(type(newDict1))

#Step:2 Nested dictionaries
emp_det = {'Employee':{'Dev':{'ID':'001',
                              'sal':'2000',
                              'Des':'Teamlead'},
                       'Eva': {'ID': '002',
                               'sal': '1000',
                               'Des': 'Associate'}
                       }}
print(emp_det)

#step 3: performing operations on hash tables
#type1: key value
print(myDict['Dave'])#001

print(myDict.keys())#(['Dave', 'Ava', 'Joe'])
print(myDict.values())#(['001', '002', '003'])
print(myDict.get('Ava'))#002

for x in myDict:
    print(x)#fetch keys
for x in myDict.values():
    print(x)#fetch values

for x,y in myDict.items():
    print(x,y)

for x in myDict.items():
    print(x)

#step 4: performing operations on Hash tables
#updating
myDict['Dave']='004'
myDict['Chris']='003'
print(myDict)

#delete
myDict.pop('Ava')
print(myDict)

myDict.popitem()
print(myDict)

del myDict['Dave']
print(myDict)


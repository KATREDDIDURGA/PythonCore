trave = input('y or n')
while trave  == 'y':
    num = int(input('number of people'))
    for num in range(1,num+1):
        name = input("name:")
        age = input("age:")
        sex = input("sex:")
        print(name,":",age,":",sex)
    trave = input('oops! forgot someone')
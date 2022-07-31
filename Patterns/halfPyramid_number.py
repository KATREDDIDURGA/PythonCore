'''
rows = 5
spaces = 0
numbers = rows
'''

def pyr(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        print("\n")
pyr(5)
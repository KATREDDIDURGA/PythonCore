'''
rows = 5
spaces = 4,3,2,1,0
stars  = 1,3,5,7,9...
'''
for j in range(1,5+1):
    for k in range(1,5-j+1):
        print(" ",end="")
    for k in range(0,j):
        print("*",end="")
    for k in range(0,j-1):
        print("*", end="")
    print("\n")

'''
rows = 5
spaces = 0
stars = 5,4,3,2,1
'''
def invHalf(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("* ",end=" ")
        print("\n")

invHalf(5)
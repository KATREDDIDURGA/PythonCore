'''
rows = 5
spaces = 0
stars = 1,2,3,4,5
'''
def patr(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print("\n")
patr(5)
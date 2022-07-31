'''
rows = n
spaces = n-1,n-2,n-3...,n-row
stars = 1,3,5,7,9....
'''
#for loop iterate  n times
def patt(n):
    for i in range(0,n):
        #spaces
        for j in range (0,n-i):
            print(end = ' ')

        for j in range(0,2*i-1):
            print("*",end = "")
            j = j+1
        print("\n")
patt(5)

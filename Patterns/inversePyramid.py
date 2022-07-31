'''
rows = 5
spaces = 0,1,2,3,4,5
stars = 2(5)+1
'''
def inv(n):
    k = 2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k +=1
        for j in range(0,i+1):
            print("* ",end="")

        print("\r")
inv(5)
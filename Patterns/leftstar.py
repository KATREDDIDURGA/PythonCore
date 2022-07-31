def leftstar(n):
    k =2*n-2
    for i in range(n+1,1,-1):
        for j in range(0,i-1):
            print(" ",end="")
        for j in range(i,n+1):
            print("*",end="")
        print("\r")
    for i in range(0,n):
        for j in range(n+i,n,-1):
            print(" ",end="")
        for j in range(n,i,-1):
            print("*",end="")
        print("\r")
leftstar(5)
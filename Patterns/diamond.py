def hg(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print(" ", end="")
        for j in range(n-i,0,-1):
            print("* ", end="")
        # for j in range(i-1,n-1):
        #     print("*", end="")
        print("\r")
    for i in range(1,n):
        for j in range(i+1):
            print(" ",end="")
        for j in range(n-i,0,-1):
            print("* ", end="")
        # for j in range(n-i,0,-1):
        #     print("*", end="")

        print("\r")






hg(5)
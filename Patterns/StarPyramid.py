def pattern(n):
    space = 2*n
    for i in range(0,n):
        for j in range(0,space):
            print(end=' ')
        space = space-1
        for j in range(0,i+1):
            print("* ",end=' ')
        print('\n')

pattern(5)
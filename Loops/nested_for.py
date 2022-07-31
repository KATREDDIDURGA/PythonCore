from math import sqrt
n = int(input("max num"))
for a in range(1,n+1):
    for b in range(a,n):
        c_sq = a**2+b**2
        c = int(sqrt(c_sq))
        if((c_sq - c**2) == 0):
            print(a,b,c)
def alphane(n):
    chara = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(chara),end='')
            chara+=1
        print("\n")

alphane(5)
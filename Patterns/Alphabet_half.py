'''
rows = 5
spaces = 0
characters = 65,66 66, 67 67 67, 68 68 68 68....
'''

def cha(n):
    charac = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(charac),end=' ')
        charac +=1
        print("\n")
cha(5)
